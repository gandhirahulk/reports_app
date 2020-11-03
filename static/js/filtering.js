$('input[type="checkbox"]').change(function (e) {
    $(document.getElementById('partial_select_await')).on('click', function () {
        $('#checkboxes input:checkbox').each(function () {
            if ($(this).attr('id').includes('-select')) {
                let class_name = this.id.split('-')[0]
                let selected_elements = document.getElementsByClassName(class_name)
                let checked = 0;
                let total = 0;
                for (let i = 0; i < selected_elements.length; i++) {
                    if (selected_elements[i].checked == true) {
                        checked += 1;
                    }
                    if (selected_elements[i].parentElement.style.display == 'block') {
                        total += 1
                    }
                }
                if (checked == 0) {
                    this.checked = false;
                    $(this).prop({indeterminate: false});
                } else if (checked == total) {
                    this.checked = true;
                    $(this).prop({indeterminate: false});
                } else if (checked != total) {
                    this.checked = false;
                    $(this).prop({indeterminate: true});
                }
            }

        });
    });
});


// initialize count for selected companies
function initialize_field_count() {
    let class_names = [];
    $('#checkboxes input:checkbox').each(function () {
        let class_name = $(this).attr('class');
        if (class_name != null && !class_names.includes(class_name)) {
            class_names.push(class_name);
        }

    });

    $(document.getElementById('partial_select_await')).trigger("click");
}

// trigger initialize count function on windows load
window.onload = initialize_field_count;


//render filtered fields based on selection
function render_filtered_fields(data) {
    $("input:checkbox").each(function () {
        $(this).parent().css('display', 'block');
    });

    $("input:checkbox").each(function () {
        jQuery.each(data, function (key, values) {
            let all_checkboxes = document.getElementsByClassName(key);
            for (let j = 0; j < all_checkboxes.length; j++) {
                let id_without_suffix = all_checkboxes[j].id.split("--")[2];
                if (!values.includes(id_without_suffix)) {
                    $(all_checkboxes[j]).parent().css('display', 'none');
                    all_checkboxes[j].checked = false;
                }
            }
            if (key === "no-selections-made") {
                $("input:checkbox").each(function () {
                    $(this).parent().css('display', 'block');
                });
            }
        });
    });
    initialize_field_count()
}

// fetch fields
function fetch_dependent_field(current_id) {
    console.log(current_id)
    let class_name_to_id_map = new Map();
    let condition = $("#" + current_id).prop('checked');
    let current_class_name = $('#' + current_id).attr('class');
    let selected_checkboxes = [];

    if (current_class_name != null) {
        $('#checkboxes input:checked').each(function () {
            if ($(this).attr('id').includes('--')) {
                let checkbox_id = $(this).attr('id').split('--')[2];

                let local_class_name = $(this).attr('class');
                if (local_class_name != null) {
                    if (!class_name_to_id_map.has(local_class_name)) {

                        class_name_to_id_map.set(local_class_name, [checkbox_id]);
                    } else {
                        selected_checkboxes = class_name_to_id_map.get(local_class_name);
                        if (!selected_checkboxes.includes(checkbox_id)) {
                            selected_checkboxes.push(checkbox_id);
                        }
                    }

                }
            }
        });
        if (condition == false && class_name_to_id_map.length > 0 && class_name_to_id_map.get(current_class_name).includes(current_id)) {
            selected_checkboxes = class_name_to_id_map[current_class_name];
            let index = selected_checkboxes.indexOf(current_id);
            selected_checkboxes.splice(index, 1);
            if (selected_checkboxes.length == 0) {
                class_name_to_id_map.delete(current_class_name);
            }
        }


        let field_map = filter_records(class_name_to_id_map);
        console.log(field_map)
        if (field_map.length == 0) {
            field_map['no-selections-made'] = 0
        }
        render_filtered_fields(field_map);
    }
}


let parent_to_child_map = new Map();
parent_to_child_map.set('Department', ['Function_Category'])
parent_to_child_map.set('Function_Category', ['Team'])
parent_to_child_map.set('Team', ['Sub_Team'])
parent_to_child_map.set('Sub_Team', ['State'])
parent_to_child_map.set('State', ['City'])
parent_to_child_map.set('City', ['Location'])
parent_to_child_map.set('Location', ['Vendor'])
parent_to_child_map.set('Vendor', ['none'])


let child_to_parent_map = new Map();
child_to_parent_map.set('Vendor', 'Location')
child_to_parent_map.set('Location', 'City')
child_to_parent_map.set('City', 'State')
child_to_parent_map.set('State', 'Sub_Team')
child_to_parent_map.set('Sub_Team', 'Team')
child_to_parent_map.set('Team', 'Function_Category')
child_to_parent_map.set('Function_Category', 'Department')
child_to_parent_map.set('Department', 'none')


function filter_children(children_name, dependent_fields_map, record_ids, selected_field_array) {
    $.each(children_name, function (i, child_name) {
        if (child_name !== 'none') {
            let dependent_child_ids = fetch_dependent_children(child_name, record_ids, dependent_fields_map)
            if (selected_field_array.includes(child_name)) {
                return true;
            }
            let children_name = parent_to_child_map.get(child_name)
            filter_children(children_name, dependent_fields_map, dependent_child_ids, selected_field_array)
        }
    });
}

function fetch_dependent_children(child_name, record_ids, dependent_fields_map) {
    let child_elements = document.getElementsByClassName(child_name)
    let child_records = [];
    $.each(record_ids, function (i, record_id) {

        for (let i = 0; i < child_elements.length; i++) {
            let fk = child_elements[i].id.split('--')[1];
            if (fk === record_id && !child_records.includes(child_elements[i].id.split('--')[2])) {
                child_records.push(child_elements[i].id.split('--')[2]);
            }
        }

    })
    fill_dependent_field_map(child_name, child_records, dependent_fields_map)

    return child_records
}

function fill_dependent_field_map(field_name, dependent_ids, dependent_fields_map) {
    if (typeof dependent_fields_map[field_name] == 'undefined') {
        dependent_fields_map[field_name] = dependent_ids
    } else {

        let present_ids = dependent_fields_map[field_name]
        if (present_ids.length !== 0) {
            dependent_fields_map[field_name] = dependent_ids
        }
    }
}


function filter_records(class_name_to_id_map) {
    let field_names = ['Department', 'Function_Category', 'Team', 'Sub_Team', 'State', 'City', 'Location', 'Vendor']
    let dependent_fields_map = {}
    let selected_field_array = []
    for (let [key, value] of class_name_to_id_map) {
        selected_field_array.push(key)
    }
    let selected_fields = []
    let record_ids = []

    $.each(field_names, function (i, field) {
        if (class_name_to_id_map.has(field)) {
            selected_fields.push(field)
        }
    });

    $.each(selected_fields, function (i, field1) {
        let children_name = parent_to_child_map.get(field1)
        if (class_name_to_id_map.has(field1)) {
            record_ids = class_name_to_id_map.get(field1)
            filter_children(children_name, dependent_fields_map, record_ids, selected_field_array)
        }
    });

    $.each(selected_fields, function (i, field) {
        if (class_name_to_id_map.has(field)) {
            let record_ids = class_name_to_id_map.get(field)
            filter_parents(field, dependent_fields_map, record_ids, selected_field_array)
        }
    });
    return dependent_fields_map
}


function filter_parents(field, dependent_fields_map, record_ids, selected_field_array) {
    let parent_elements = document.getElementsByClassName(field)
    let parent_records = []
    $.each(record_ids, function (i, record_id) {
        for (let i = 0; i < parent_elements.length; i++) {
            let pk = parent_elements[i].id.split('--')[2];
            if (pk === record_id && !parent_records.includes(record_id)) {
                parent_records.push(parent_elements[i].id.split('--')[1]);
            }
        }
        let parent_name = child_to_parent_map.get(field);
        if (parent_name !== 'none') {
            fill_dependent_field_map(parent_name, parent_records, dependent_fields_map)
            dependent_fields_map[parent_name] = parent_records
            if (selected_field_array.includes(parent_name)) {
                return true;
            }
            filter_parents(parent_name, dependent_fields_map, parent_records,
                selected_field_array)
        }
    });
}