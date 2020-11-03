$(".chosen-select").chosen({
    no_results_text: "Oops, nothing found!"
})
$(".chosen-search-input").each(function (i, v) {
    v.style.width = '200px'
});
$(".chosen-choices").each(function (i, v) {
    v.style.width = '300px'
});

$('#main_table').dataTable({
    scrollX: "true",
});
$("#main_table").hover(function () {
    $('.dataTables_scrollBody').attr('style', 'overflow: scroll !important');
});
$("#main_table").mouseout(function () {
    $('.dataTables_scrollBody').attr('style', 'overflow: hidden !important');
});

$("#payroll_form").on("submit", function (e) {
    $.post('/reports/', $(this).serialize(), function (data) {
        $('.message').html(data.message);
    });
    e.preventDefault();
});

var expanded = false;

function showCheckboxes(element_id) {
    var all = document.getElementsByClassName("checklist-dropdown");
    var len = all.length;
    for (i = 0; i < len; i++) {
        all[i].style.display = "none";
        expanded = false
    }
    var checkboxes = document.getElementById(element_id);
    if (!expanded) {
        checkboxes.style.display = "block";
        expanded = true;
    } else {
        checkboxes.style.display = "none";
        expanded = false;
    }
}


$(document).ready(function () {
    let elements = document.getElementsByClassName("MultiCheckBoxDetail")
    $.each(elements, function (i, v) {
        v.style.position = 'relative';
        v.style.background = 'white';
        v.style.width = '230px';
        v.style.zIndex = '9'
    });

    $('.dataTables_scrollBody').attr('style', 'overflow: hidden !important');
    $(document).keyup(function (e) {
        if (e.keyCode == 27) {
            var all = document.getElementsByClassName("checklist-dropdown");
            var len = all.length;
            for (i = 0; i < len; i++) {
                all[i].style.display = "none";
            }
        }
    });
    $(window).click(function (e) {
        var all = document.getElementsByClassName("checklist-dropdown");
        var len = all.length;
        for (i = 0; i < len; i++) {
            if (e.target.id == 'tab_content' || e.target.id == 'response_header' || e.target.id == 'payroll_form') {
                all[i].style.display = "none";
            }

        }
    });


    $(document).on("click", ".MultiCheckBox", function () {


        var detail = $(this).next();
        detail.show();
    });

    $(document).on("click", ".MultiCheckBoxDetailHeader input", function (e) {
        e.stopPropagation();
        var hc = $(this).prop("checked");
        $(this).closest(".MultiCheckBoxDetail").find(".MultiCheckBoxDetailBody input").prop("checked", hc);
        $(this).closest(".MultiCheckBoxDetail").next().UpdateSelect();
    });

    $(document).on("click", ".MultiCheckBoxDetailHeader", function (e) {
        var inp = $(this).find("input");
        var chk = inp.prop("checked");
        inp.prop("checked", !chk);
        $(this).closest(".MultiCheckBoxDetail").find(".MultiCheckBoxDetailBody input").prop("checked", !chk);
        $(this).closest(".MultiCheckBoxDetail").next().UpdateSelect();
    });

    $(document).on("click", ".MultiCheckBoxDetail .cont input", function (e) {
        e.stopPropagation();
        $(this).closest(".MultiCheckBoxDetail").next().UpdateSelect();

        var val = ($(".MultiCheckBoxDetailBody input:checked").length == $(".MultiCheckBoxDetailBody input").length)
        $(".MultiCheckBoxDetailHeader input").prop("checked", val);
    });

    $(document).on("click", ".MultiCheckBoxDetail .cont", function (e) {
        var inp = $(this).find("input");
        var chk = inp.prop("checked");
        inp.prop("checked", !chk);

        var multiCheckBoxDetail = $(this).closest(".MultiCheckBoxDetail");
        var multiCheckBoxDetailBody = $(this).closest(".MultiCheckBoxDetailBody");
        multiCheckBoxDetail.next().UpdateSelect();

        var val = ($(".MultiCheckBoxDetailBody input:checked").length == $(".MultiCheckBoxDetailBody input").length)
        $(".MultiCheckBoxDetailHeader input").prop("checked", val);
    });

    $(document).mouseup(function (e) {
        var container = $(".MultiCheckBoxDetail");
        if (!container.is(e.target) && container.has(e.target).length === 0) {
            container.hide();
        }
    });
});

var defaultMultiCheckBoxOption = {width: '220px', defaultText: 'Select Below', height: '200px'};

jQuery.fn.extend({
    CreateMultiCheckBox: function (options) {

        var localOption = {};
        localOption.width = (options != null && options.width != null && options.width != undefined) ? options.width : defaultMultiCheckBoxOption.width;
        localOption.defaultText = (options != null && options.defaultText != null && options.defaultText != undefined) ? options.defaultText : defaultMultiCheckBoxOption.defaultText;
        localOption.height = (options != null && options.height != null && options.height != undefined) ? options.height : defaultMultiCheckBoxOption.height;

        this.hide();
        this.attr("multiple", "multiple");
        var divSel = $("<div class='MultiCheckBox'>" + localOption.defaultText + "<span class='k-icon k-i-arrow-60-down'><svg aria-hidden='true' focusable='false' data-prefix='fas' data-icon='sort-down' role='img' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 320 512' class='svg-inline--fa fa-sort-down fa-w-10 fa-2x'><path fill='currentColor' d='M41 288h238c21.4 0 32.1 25.9 17 41L177 448c-9.4 9.4-24.6 9.4-33.9 0L24 329c-15.1-15.1-4.4-41 17-41z' class=''></path></svg></span></div>").insertBefore(this);
        divSel.css({"width": localOption.width});

        var detail = $("<div class='MultiCheckBoxDetail'><div class='MultiCheckBoxDetailHeader'><input type='checkbox' class='mulinput' value='-1982' /><div>Select All</div></div><div class='MultiCheckBoxDetailBody'></div></div>").insertAfter(divSel);
        detail.css({"width": parseInt(options.width) + 10, "max-height": localOption.height});
        var multiCheckBoxDetailBody = detail.find(".MultiCheckBoxDetailBody");

        this.find("option").each(function () {
            var val = $(this).attr("value");

            if (val == undefined)
                val = '';

            multiCheckBoxDetailBody.append("<div class='cont'><div><input type='checkbox' class='mulinput' value='" + val + "' /></div><div>" + $(this).text() + "</div></div>");
        });

        multiCheckBoxDetailBody.css("max-height", (parseInt($(".MultiCheckBoxDetail").css("max-height")) - 28) + "px");
    },
    UpdateSelect: function () {
        var arr = [];

        this.prev().find(".mulinput:checked").each(function () {
            arr.push($(this).val());
        });

        this.val(arr);
    },
});


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