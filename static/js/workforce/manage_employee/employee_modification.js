

window.addEventListener("load", function () {
    document.getElementById('curaddress').value = '';
    document.getElementById('peraddress').value = '';
})

function check_validity(element_id) {
    let level = element_id.split('--')[1]
    let d1 = document.getElementById('from_date--' + level).value
    let d2 = document.getElementById('to_date--' + level).value

    if (d1 > d2 && d1 != '' && d2 != '') {
        set_error(element_id, "'from date' should be less than 'to date'")
    } else {
        set_success(element_id);
    }
}

function restrict_date(date_id) {
    let doj = document.getElementById('doj').value
    let dor = document.getElementById('dor').value
    let dol = document.getElementById('dol').value
    if (date_id == 'doc') {
        if (doj == '' && dor == '' && dol == '') {
            set_max_date(date_id)
        }

    } else if (date_id == 'doj') {
        if (dor == '' && dol == '') {
            set_max_date(date_id)
        }

    } else if (date_id == 'dor') {
        if (dol == '') {
            set_max_date(date_id)
        }

    } else if (date_id == 'dol') {
        set_max_date(date_id)

    }
}

function validate_dates(date_id) {
    let doj = document.getElementById('doj').value
    let doc = document.getElementById('doc').value
    let dor = document.getElementById('dor').value
    let dol = document.getElementById('dol').value
    if (date_id == 'doc') {
        document.getElementById('doj').setAttribute("min", doc);
        document.getElementById('dor').setAttribute("min", doc);
        document.getElementById('dol').setAttribute("min", doc);

    } else if (date_id == 'doj') {
        document.getElementById('doc').setAttribute("max", doj);
        document.getElementById('dor').setAttribute("min", doj);
        document.getElementById('dol').setAttribute("min", doj);

    } else if (date_id == 'dor') {
        document.getElementById('doj').setAttribute("max", dor);
        document.getElementById('doc').setAttribute("max", dor);
        document.getElementById('dol').setAttribute("min", dor);


    } else if (date_id == 'dol') {
        document.getElementById('doc').setAttribute("max", dol);
        document.getElementById('doj').setAttribute("max", dol);
        document.getElementById('dor').setAttribute("max", dol);

    }

}

function calculate_exp(element_id) {
    let level = element_id.split("--")[1]
    let months;
    let d1 = document.getElementById('from_date--' + level).value
    let d2 = document.getElementById('to_date--' + level).value
    let date1 = d1.split("-");
    let date2 = d2.split('-');
    months = (date2[0] - date1[0]) * 12;
    months = Number(months) + Number(date2[1]) - Number(date1[1]);
    document.getElementById('exp--' + level).value = months <= 0 ? 0 : months;
}

function check_duplicate(eid, element_id) {
    let fd = new FormData();
    fd.append('id', eid);
    fd.append('csrfmiddlewaretoken', csrf_token);
    $.ajax({
        url: '/workforce/manageemployee/check_duplicate_eid/',
        method: 'POST',
        data: fd,
        dataType: 'text',
        contentType: false,
        processData: false,
        success: function (data) {
            if (data) {
                if (data == 'yes') {
                    set_error(element_id, "duplicate id")
                } else {
                    set_success(element_id)
                }
            } else {
                alert("ajax call not success.");
            }
        },
        fail: function () {
            alert('request failed');
        }
    });

}

//set max available date to select to today
function set_max_date(date_id) {
    let today = new Date();
    let dd = today.getDate();
    let mm = today.getMonth() + 1;
    const yyyy = today.getFullYear();
    if (dd < 10) {
        dd = '0' + dd
    }
    if (mm < 10) {
        mm = '0' + mm
    }
    today = yyyy + '-' + mm + '-' + dd;
    document.getElementById(date_id).setAttribute("max", today);
}

//validate joining resignation and leaving dates
function validate_date(date_id) {
    let today = new Date();
    let dd = today.getDate();
    let mm = today.getMonth() + 1;
    let yyyy = today.getFullYear();
    if (dd < 10) {
        dd = '0' + dd
    }
    if (mm < 10) {
        mm = '0' + mm
    }
    yyyy = yyyy - 18;
    let begin_year = today.getFullYear() - 100;
    let begin_date = begin_year + '-' + mm + '-' + dd;
    document.getElementById(date_id).setAttribute("min", begin_date);

    if (date_id.includes('mother') || date_id.includes('father')) {
        yyyy = yyyy - 36;
    }
    if (date_id.includes('child')) {
        yyyy = today.getFullYear();
        let emp_dob = document.getElementById('empdob').value;
        let emp_dd = emp_dob.split('-')[2];
        let emp_mm = emp_dob.split('-')[1];
        let emp_yyyy = emp_dob.split('-')[0];
        emp_yyyy = Number(emp_yyyy) + 18;
        let min_child_dob = emp_yyyy + '-' + emp_mm + '-' + emp_dd;
        document.getElementById(date_id).setAttribute("min", min_child_dob);
    }
    today = yyyy + '-' + mm + '-' + dd;
    document.getElementById(date_id).setAttribute("max", today);

}


//open sections on click
function openSection(section, activesection, plmin) {
    try {
        var x = document.getElementsByClassName('showsection');
        var y = document.getElementsByClassName('fa-minus-circle');
        var z = document.getElementsByClassName('active_section');
        document.getElementById(section).classList.toggle('hidesection');
        document.getElementById(section).classList.toggle('showsection');
        document.getElementById(activesection).classList.toggle('active_section');
        document.getElementById(plmin).classList.toggle('fa-plus-circle');
        document.getElementById(plmin).classList.toggle('fa-minus-circle');
        console.log(document.getElementById(plmin).classList);
    } catch (TypeError) {
        console.log('caught error');
    }

}

$(document).ready(function () {
    $("#sameaddress").on("click", function () {
        if (this.checked) {
            $("#curaddress").val($("#peraddress").val());
            $("#curcountry").val($("#percountry").val());
            $("#curcity").val($("#percity").val());
            $("#curstate").val($("#perstate").val());
            $("#curpin").val($("#perpin").val());
        } else {
            $("#curaddress").val('');
            $("#curcountry").val('');
            $("#curcity").val('');
            $("#curstate").val('');
            $("#curpin").val('');
        }
    });


    $(function () {
        console.log('date picker');
        $("#empdob").datepicker();
    });

    $("#empdob").on("focus", function () {
        $("#empdob").datepicker();
        $("#empdob").datepicker("show");

    });
});

let selected_filed_to_id_map = new Map()

selected_filed_to_id_map = {
    'empselectedcompany': [],
    'empselectedbusiness': [],
    'empselectedfunction': [],
    'empselectedsubfunction': [],
    'empselectedrole': [],
    'empselectedregion': [],
    'empselectedstate': [],
    'empselectedlocation': [],
    'empselectedvendor': [],
    'empselectedsubloc': [],
    'empselecteddesg': []
}

let parents_map = new Map()

parents_map = {
    'empselectedcompany': [],
    'empselectedbusiness': ['empselectedcompany'],
    'empselectedfunction': ['empselectedcompany', 'empselectedbusiness'],
    'empselectedsubfunction': ['empselectedcompany', 'empselectedbusiness', 'empselectedfunction'],
    'empselectedrole': ['empselectedcompany', 'empselectedbusiness', 'empselectedfunction', 'empselectedsubfunction'],
    'empselectedregion': ['empselectedcompany'],
    'empselectedstate': ['empselectedcompany', 'empselectedregion'],
    'empselectedlocation': ['empselectedcompany', 'empselectedregion', 'empselectedstate'],
    'empselectedvendor': ['empselectedcompany'],
    'empselectedsubloc': ['empselectedlocation', 'empselectedcompany', 'empselectedregion', 'empselectedstate'],
    'empselecteddesg': ['empselectedrole', 'empselectedcompany', 'empselectedbusiness', 'empselectedfunction', 'empselectedsubfunction']
}

count = 0
function show_hide_dependent_options(element_id) {
    if (count > 3) {
        return;
    }
    count++;

        $.each(selected_filed_to_id_map, function (k, v) {
            if (!parents_map[element_id].includes(k) && k != element_id) {
                console.log('key: ' + k);
                if (v.length > 0) {
                    $('#' + k + ' option').each(function (index, element) {
                        if ($(element).attr('value') === '') {
                            return true;
                        } else if (!v.includes(element.value)) {
                            $(element).hide();
                        } else if (v.includes(element.value)) {
                            $(element).show();
                            $('#' + k).val(element.value)
                            console.log('fuck' + ":" + k);
                            change_of_field.call(document.getElementById(k));
                            $('#' + k).val('')

                        }
                    });
                }
            }
        });

}

function create_map_utilities() {
    let parent_to_child_id_map = new Map();
    parent_to_child_id_map = {
        'empselectedcompany': ['empselectedvendor', 'empselectedbusiness', 'empselectedregion'],
        'empselectedbusiness': ['empselectedfunction'],
        'empselectedfunction': ['empselectedsubfunction'],
        'empselectedsubfunction': ['empselectedrole'],
        'empselectedrole': ['empselecteddesg'],
        'empselectedregion': ['empselectedstate'],
        'empselectedstate': ['empselectedlocation'],
        'empselectedlocation': ['empselectedsubloc']
    }

    let child_to_parent_map = new Map();
    child_to_parent_map = {
        'empselectedbusiness': ['empselectedcompany'],
        'empselectedfunction': ['empselectedbusiness'],
        'empselectedsubfunction': ['empselectedfunction'],
        'empselectedrole': ['empselectedsubfunction'],
        'empselecteddesg': ['empselectedrole'],
        'empselectedregion': ['empselectedcompany'],
        'empselectedstate': ['empselectedregion'],
        'empselectedlocation': ['empselectedstate'],
        'empselectedsubloc': ['empselectedlocation']
    }
    return {parent_to_child_id_map, child_to_parent_map};
}

function reset_selection_map() {
    $.each(selected_filed_to_id_map, function (k, v) {
        v=[];
        selected_filed_to_id_map[k] = v;
    });
}

function fill_selections_map(child_array, filter) {
    child_array.forEach(function (value1, value2) {
        $('#' + value1 + ' option').each(function (index, element) {
            if ($(element).attr('value') === '') {
                return true;
            } else if ($(element).attr('id').split('--')[1] == filter) {
                if (!selected_filed_to_id_map[value1].includes($(element).val())) {
                    selected_filed_to_id_map[value1].push($(element).val());
                }
            }
        });
    });
}

function change_of_field() {
    let {parent_to_child_id_map, child_to_parent_map} = create_map_utilities();

    if (parent_to_child_id_map[this.id] == null) {
        return;
    }
    let child_array = parent_to_child_id_map[this.id];
    let filter = $(this).val();
    fill_selections_map(child_array, filter);
    show_hide_dependent_options(this.id);
}

$('.position_select').change(function () {
    if(this.value ==='' && this.id == 'empselectedcompany'){
        $('.position_select').each(function (e,v) {
        $('#' + v.id + ' option').each(function (index, element) {
            $(element).show();
        });
    });
    }
    change_of_field.call(this);
    reset_selection_map();
    count = 0;
});
