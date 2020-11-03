let sidebar = document.getElementById("sidebar");


function hide_edit_modals() {
    let arrayOfElements = document.getElementsByClassName('edit_company_form_modal');
    let lengthOfArray = arrayOfElements.length;
    for (let i = 0; i < lengthOfArray; i++) {
        arrayOfElements[i].style.display = 'none';
    }
}

function hide_create_modals() {
    $("#create_company_modal").css("display", "none");
    $("#create_vendor_modal").css("display", "none");
    $("#create_business_modal").css("display", "none");
    $("#create_location_modal").css("display", "none");
    $("#create_sub_location_modal").css("display", "none");
    $("#create_function_modal").css("display", "none");
    $("#create_sub_function_modal").css("display", "none");
    $("#create_role_modal").css("display", "none");
    $("#create_designation_modal").css("display", "none");
    $("#create_region_modal").css("display", "none");
    $("#create_state_modal").css("display", "none");
    $("#create_team_modal").css("display", "none");
    $("#create_group_modal").css("display", "none");
    $("#create_gender_modal").css("display", "none");
}

$(document).keyup(function () {
    if (event.keyCode === 27) {
        hide_create_modals()
        hide_edit_modals();
        $("#view_designation_form").css("display", "none");
        $("#delete_record").css("display", "none");
        $("#sidebar").css("z-index", 100);
    }
});


$(window).click(function (e) {
    if (e.target.id === 'create_company_modal' ||
        e.target.id === 'create_vendor_modal' ||
        e.target.id === 'create_business_modal' ||
        e.target.id === 'create_location_modal' ||
        e.target.id === 'create_sub_location_modal' ||
        e.target.id === 'create_function_modal' ||
        e.target.id === 'create_sub_function_modal' ||
        e.target.id === 'create_role_modal' ||
        e.target.id === 'create_designation_modal' ||
        e.target.id === 'create_region_modal' ||
        e.target.id === 'create_state_modal' ||
        e.target.id === 'create_team_modal' ||
        e.target.id === 'create_group_modal' ||
        e.target.id === 'create_gender_modal' ||

        e.target.className === 'edit_company_form_modal' ||

        e.target.id === 'delete_record' ||

        e.target.id === 'view_designation_form') {

        hide_create_modals();
        $("#view_designation_form").css("display", "none");
        hide_edit_modals();
        $("#delete_record").css("display", "none");
        $("#sidebar").css("z-index", 100);
    }
});


function render_select_options(select_id, sub_select_array) {
    $('#' + select_id).change(function () {
        let filter = $(this).val();
        let child = $('#' + sub_select_array[0] + ' option')
        let total = child.length;
        let count = 0;
        child.each(function () {
            if (this.id.split('--')[1] === filter) {
                $('#' + sub_select_array[0]).attr("disabled", false);
                $(this).show();
            } else {
                $(this).hide();
                count += 1;
            }
            sub_select_array.forEach(function (select_id, index) {
                $('#' + select_id).val('');
            });
        });
        if (count === total) {
            console.log(sub_select_array[0])
            $('#' + sub_select_array[0]).attr("disabled", true)
        }
    });
}



