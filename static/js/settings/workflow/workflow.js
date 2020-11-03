window.addEventListener("load", function () {
    $('.remove').click(function () {
        var n = $('#levels-table tr').length;
        // alert(n);
        if (n > 1) {
            $(this).closest('tr').remove();
        }
    })

    // let inputs = $('#Workflow :input');
    // inputs.each(function () {
    //     $(this).val('');
    // });
})

// enable disable employee select
function hide_show_employee_selection(element_id) {
    let level_number = element_id.split('--')[1];
    if (document.getElementById(element_id).value == "Other") {
        $("#emp_code--" + level_number).css("display", "block");
    } else {
        $("#emp_code--" + level_number).css("display", "none");
    }
}

function hide_show_constraints(element_id) {
    let level_number = element_id.split('--')[1];
    if (document.getElementById(element_id).value == "self") {
        $("#intimation_label--" + level_number).css("display", "none");
        $("#period_div--" + level_number).css("display", "none");
        $("#intimation--" + level_number).css("display", "none");
    } else {
        $("#intimation_label--" + level_number).css("display", "");
        $("#period_div--" + level_number).css("display", "block");
        $("#intimation--" + level_number).css("display", "");
    }
}

function make_period_mandatory(element_id) {
    let level_number = element_id.split('--')[1];
    if ($('#' + element_id).val() == '1' || $('#' + element_id).val() == '2') {
        document.getElementById("period_value--" + level_number).required = true;
        document.getElementById("period_type--" + level_number).required = true;
    } else {
        document.getElementById("period_value--" + level_number).required = false;
        document.getElementById("period_type--" + level_number).required = false;
    }
}


// enable disable on intimation click
function hide_show_inputs(element_id) {
    let level_number = element_id.split('--')[1];
    if ($('#' + element_id).is(':checked')) {
        $("#period_value--" + level_number).prop("disabled", true);
        $("#period_type--" + level_number).prop("disabled", true);
        $("#auto_action--" + level_number).prop("disabled", true);
        $("#period_label--" + level_number).css("color", "gray");
        $("#period_type_label--" + level_number).css("color", "gray");
        $("#auto_action_label--" + level_number).css("color", "gray");
        $("#period_value--" + level_number).css('cursor', 'not-allowed');
        $("#period_type--" + level_number).css('cursor', 'not-allowed');
        $("#auto_action--" + level_number).css('cursor', 'not-allowed');
        $("#period_label--" + level_number).css('cursor', 'not-allowed');
        $("#period_type_label" + level_number).css('cursor', 'not-allowed');
        $("#auto_action_label--" + level_number).css('cursor', 'not-allowed');
        $('#auto_action--' + level_number).val('3');
    } else {
        $("#period_value--" + level_number).prop("disabled", false);
        $("#period_type--" + level_number).prop("disabled", false);
        $("#auto_action--" + level_number).prop("disabled", false);
        $("#period_label--" + level_number).css("color", "");
        $("#period_type_label--" + level_number).css("color", "");
        $("#auto_action_label--" + level_number).css("color", "");
        $("#period_value--" + level_number).css('cursor', 'default');
        $("#period_type--" + level_number).css('cursor', 'default');
        $("#auto_action--" + level_number).css('cursor', 'default');
        $("#period_label--" + level_number).css('cursor', 'default');
        $("#period_type_label" + level_number).css('cursor', 'default');
        $("#auto_action_label--" + level_number).css('cursor', 'default');
        $('#auto_action--' + level_number).val('');
    }
}

function insert_new_cloned_element(amount, level_division) {
    let new_amount = amount + 1;
    let cloned_div = $('#' + level_division + amount.toString()).clone();
    cloned_div.insertAfter('#' + level_division + amount.toString());

    let cloned_div_id = cloned_div.prop('id');
    cloned_div.prop('id', cloned_div_id.replace("--" + amount, "--" + new_amount));


    cloned_div.find('[id$="--' + amount + '"]').each(function (index, child) {
        if (child.hasAttribute('id')) {
            child.id = child.id.replace("--" + amount, "--" + new_amount);
        }
        if (child.hasAttribute('name')) {
            child.name = child.name.replace("--" + amount, "--" + new_amount);
        }
        if (child.hasAttribute('className') && child.className.includes('--')) {
            child.className = child.className.replace("--" + amount, "--" + new_amount);
        }
    });
    return new_amount;
}

function remove_headings_from_cloned_element(class_name, new_amount) {
    if (class_name === 'exp_div_class') {
        $('#exp_first_row--' + new_amount).remove();
        $('#addexp--' + new_amount).css("visibility", 'hidden');
    }



    if (class_name === 'od_div_class') {
        $('#od_first_row--' + new_amount).remove();
        $('#add_od--' + new_amount).css("visibility", 'hidden');

    }

    if (class_name === 'qual_div_class') {
        $('#qual_first_row--' + new_amount).remove();
        $('#addqualification--' + new_amount).css("visibility", 'hidden');
    }
    if (class_name === 'child_div_class') {
        $('#child_first_row--' + new_amount).remove();
        $('#addnewchild--' + new_amount).css("visibility", 'hidden');
    }
    if (class_name === 'level_div_class') {
        document.getElementById("legend--" + new_amount).innerText = "Level " + new_amount
    }

    else{
        $('#leave_first_row--' + new_amount).remove();
        $('#add_leave--' + new_amount).css("visibility", 'hidden');
    }
}

function reset_selections(class_name, new_amount) {
    if (class_name === 'exp_div_class') {
        document.getElementById('companyName--' + new_amount).value = '';
        document.getElementById('from_date--' + new_amount).value = '';
        document.getElementById('to_date--' + new_amount).value = '';
        document.getElementById('exp--' + new_amount).value = '';
        document.getElementById('jobRole--' + new_amount).value = '';
        document.getElementById('designation--' + new_amount).value = '';
        document.getElementById('ctc--' + new_amount).value = '';


    }
    if (class_name === 'child_div_class') {
        document.getElementById('childdob--' + new_amount).value = '';
        document.getElementById('childgender--' + new_amount).value = '';
        document.getElementById('childname--' + new_amount).value = '';
    }
    if (class_name === 'qual_div_class') {
        document.getElementById('emp_selected_qualification--' + new_amount).value = '';
        document.getElementById('emp_selected_mode--' + new_amount).value = '';
        document.getElementById('yop--' + new_amount).value = '';
        document.getElementById('school--' + new_amount).value = '';
        document.getElementById('university--' + new_amount).value = '';
        document.getElementById('grade--' + new_amount).value = '';
        document.getElementById('percentage--' + new_amount).value = '';

    }
    if (class_name === 'level_div_class') {
        document.getElementById('search_emp_list--' + new_amount).value = '';
        document.getElementById('period_value--' + new_amount).value = '';
        document.getElementById('emp_code--' + new_amount).style.display = 'none';
        document.getElementById('role-select--' + new_amount).value = '';
    }

    if (class_name === 'od_div_class') {
        document.getElementById('od_type--' + new_amount).value = '';
        document.getElementById('od_count_month--' + new_amount).value = '';
        document.getElementById('hd_od--' + new_amount).checked = false
        document.getElementById('max_od_count_request--' + new_amount).value = '';
        document.getElementById('max_back_date--' + new_amount).value = '';
        document.getElementById('max_future_date--' + new_amount).value = '';
        document.getElementById('backdated_days--' + new_amount).value = '';
        document.getElementById('cancellation--' + new_amount).checked = false;
    }
}

function set_alert(message) {
    let $alert = $('#alerts--1');
    if ($alert.is(":visible")) {
        return;
    }
    let $alert_table = $('#warning-tbl--1' + ' tbody');
    $alert_table.find("tr:gt(0)").remove();
    $alert_table.append('<tr><td style="border-bottom: none;">' + message + '</td></tr>');
    $alert.show();
    setTimeout(function () {
        $alert.hide();
    }, 5000);
}

function nextLevel(level_division, class_name) {
    let amount = get_number_of_exisiting_divisions(class_name);
    if (amount > 6) {
        let message = 'Max levels reached';
        set_alert(message);
    } else {
        let new_amount = insert_new_cloned_element(amount, level_division);
        remove_headings_from_cloned_element(class_name, new_amount);
        reset_selections(class_name, new_amount);
    }
}

function reset_ids_of_all_elements(division_id, amount) {
    let div_id_with_dash = division_id + '--';
    $('*[id*=' + div_id_with_dash + ']').each(function (index, child) {
        let everyChild = document.querySelectorAll('#' + child.id + ' *');
        let id_number = child.id.split("--")[1];
        for (let i = 0; i < everyChild.length; i++) {
            if (everyChild[i].hasAttribute('id')) {
                if (everyChild[i].id.includes('--')) {
                    everyChild[i].id = everyChild[i].id.replace("--" + id_number, "--" + amount);
                    if (everyChild[i].id.includes('legend')) {
                        document.getElementById('legend--' + amount).innerText = 'Level ' + amount
                    }
                }
            }
            if (everyChild[i].hasAttribute('name')) {
                if (everyChild[i].name.includes('--')) {
                    everyChild[i].name = everyChild[i].name.replace("--" + id_number, "--" + amount);
                }
            }
            if (everyChild[i].hasAttribute('class')) {
                if (everyChild[i].className.includes('--')) {
                    everyChild[i].className = everyChild[i].className.replace("--" + id_number, "--" + amount);
                }
            }
        }
        child.id = child.id.replace("--" + id_number, "--" + amount);
        amount += 1;
    });
    return amount;
}

function get_number_of_exisiting_divisions(class_name) {
    console.log($('div.' + class_name))
    let amount = $('div.' + class_name).length;
    if (class_name === 'child_div_class') {
        amount = amount + 3
    }
    return amount;
}

function empty_first_row(division_id, element_id) {
    let parent_id = "#" + division_id + "--" + element_id.split("--")[1] + " :input"
    $(parent_id).each(function (index_value, node_value) {
        if (node_value.id != '') {
            document.getElementById(node_value.id).value = ''
        }
    });
    let message = "Cannot Remove The First Level";
    set_alert(message);
}

function removeLevel(element_id, class_name, division_id) {
    let amount = get_number_of_exisiting_divisions(class_name);
    if (amount < 2) {
        empty_first_row(division_id, element_id);

    } else {
        let div_number = element_id.split("--")[1];

        if (div_number === 1 && class_name != 'child_div_class') {
            let message = "Cannot Remove The First Level";
            set_alert(message);
        } else if (div_number === 4 && class_name == 'child_div_class') {
            empty_first_row(division_id, element_id)
        } else {
            let div_id = division_id + '--' + div_number;

            $('#' + div_id).remove();
            let amount = 1;
            if (class_name === 'child_div_class') {
                amount = amount + 3
            }
            amount = reset_ids_of_all_elements(division_id, amount);
        }
    }
}


function hidediv() {
    $('#alerts').removeClass('animate__animated animate__slideOutRight animate__fast').show().addClass('animate__animated animate__slideInRight animate__fast');

    $('#alerts').removeClass('animate__animated animate__slideInRight animate__fast').addClass('animate__animated animate__slideOutRight animate__fast');
}

setTimeout("hidediv()", 3000);
