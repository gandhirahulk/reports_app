$("#module-dropdown").change(function () {
    document.getElementById('action-dropdown').selectedIndex = 0;
    show_hide_buttons();
    $("table[id*='table--']").css("display", "none");
    reset_page_state();
});

$("#section-dropdown").change(function () {
    document.getElementById('action-dropdown').selectedIndex = 0;
    show_hide_buttons();

    const filter = $(this).val();
    let section_number = document.getElementById("section-dropdown").length;
    if (filter == '') {
        $("table[id*='table--']").css("display", "none");
    }
    reset_page_state();
    for (let i = 1; i <= section_number; i++) {
        if (filter == i) {
            $('#table--' + filter.toString()).css("display", "inline-table");
        } else {
            $('#table--' + i.toString()).css("display", "none");
        }
    }

});

function reset_page_state() {
    $("select[class*='section--']").empty().append('<option selected="selected" value=""></option>');
    $('#select_file').val('');
    document.getElementById('details').innerHTML = '';
    document.getElementById('duplication_details').innerHTML = '';
    const all_checkboxes = document.querySelectorAll('input[type="checkbox"]');
    for (const checkbox of all_checkboxes) {
        checkbox.checked = false;
    }

}

$('#action-dropdown').change(function () {
    reset_page_state();
})


//show and hide upload and process buttons
function show_hide_buttons() {
    const module = $("#module-dropdown").val();
    const section = $("#section-dropdown").val();
    const action = $("#action-dropdown").val();
    if (module && section && action) {
        $('#upload_file').css('visibility', 'visible');
        $('#process_file').css('visibility', 'visible');
    } else {
        $('#upload_file').css('visibility', 'hidden');
        $('#process_file').css('visibility', 'hidden');
    }

    const all_checkboxes = document.querySelectorAll('input[type="checkbox"]');
    for (const checkbox of all_checkboxes) {
        checkbox.checked = false;
    }
}

// fill section drop down
function fetch_section_and_fill_dropdown(fd) {
    $.ajax({
        url: '/workforce/manageemployee/import_employees/fetch_section_list/',
        method: 'POST',
        enctype: 'multipart/form-data',
        data: fd,
        dataType: 'text',
        contentType: false,
        processData: false,
        success: function (data) {
            if (data) {
                const options = document.querySelectorAll('#section-dropdown option');
                options.forEach(o => o.remove());
                const myObj = $.parseJSON(data);
                let formOption = "";
                const sections = myObj["filtered_sections"];
                $.each(sections, function (index, section) {
                    if (index == 0) {
                        formOption += "<option value='" + "" + "' selected='true'> " + "</option>";
                        formOption += "<option value='" + section['pk_module_section_code'] + "'> " + section['section_name'] + "</option>";

                    } else {
                        formOption += "<option value='" + section['pk_module_section_code'] + "' > " + section['section_name'] + "</option>";
                    }
                });
                $('select[id="section-dropdown"]').append(formOption);
            }
        },
        fail: function () {
            console.log("error assigning sections");
        }

    })
}

// fetch sections based on module selection
function post_module_to_backend() {
    const module_id = $("#module-dropdown").val();
    let fd = new FormData();
    fd.append('csrfmiddlewaretoken', csrf_token);
    fd.append("module_id", module_id);

    // ajax request to fetch sections and fill the dropdown
    fetch_section_and_fill_dropdown(fd);
}

function update_log_download() {
    const fd = new FormData();
    fd.append("csrfmiddlewaretoken", csrf_token);
    fd.append("import_id", $("#import_id").val());

    $.ajax({
        url: '/workforce/manageemployee/import_employees/update_log/',
        method: 'POST',
        data: fd,
        dataType: 'text',
        contentType: false,
        processData: false,
        success: function () {
            // alert('success');
            console.log("update status of download of log")
        },
        fail: function () {
            console.log('request failed');
        }
    });
}

// open file upload dialog
function open_file_upload_box() {
    document.getElementById('select_file').click();
}

function assignAction() {
    const action = $("#action-dropdown").val();
    $("#action_name").attr("value", action)
}

function process_file(url, fd) {
    $.ajax({
        url: url,
        method: 'POST',
        enctype: 'multipart/form-data',
        data: fd,
        dataType: 'text',
        contentType: false,
        processData: false,
        success: function (data) {
            if (data) {
                const received_data = $.parseJSON(data);
                let formOption = "";
                const unmatched_header_Array = received_data["unmatched_headers"];
                const matched_header_array = received_data["matched_headers"];
                const file_path = received_data['file_path']
                const file_name = received_data['file_name']
                const import_id = received_data['import_id']
                let matched_count = 0;
                let total_count = 0;

                $('#file_path').val(file_path);
                $('#file_name').val(file_name);
                $('#import_id').val(import_id)

                $.each(matched_header_array, function (index, header_name) {
                    formOption += "<option value='" + header_name + "'>" + header_name + "</option>";
                    matched_count += 1;
                    total_count += 1;
                });

                $.each(unmatched_header_Array, function (index, header_name) {
                    formOption += "<option value='" + header_name + "'>" + header_name + "</option>";
                    total_count += 1;
                });
                let table_class = "section--" + fd.get('section_id');
                $('.' + table_class).append(formOption);

                $.each(matched_header_array, function (index, header_name) {
                    let trimmed_header_name = header_name.replace(" ", "-");
                    $('#' + trimmed_header_name + '--select--' + fd.get('section_id')).val(header_name);
                    $('#' + trimmed_header_name + '--checkbox--id--' + fd.get('section_id')).prop("checked", true);
                });

                display_details(matched_count, total_count);
            }
        },
        fail: function () {
            alert('request failed');
        }
    });
}

function showLoading() {
    document.getElementById("spinner").style.display = 'block';
}

function hideLoading() {
    document.getElementById("spinner").style.display = 'none';
}

// post uploaded file
function post_uploaded_file() {
    setTimeout( reset_page_state, 0 );
    showLoading();
    const fd = new FormData();
    fd.append("file", $('#select_file')[0].files[0]);
    fd.append("csrfmiddlewaretoken", csrf_token);
    fd.append("module_id", $("#module-dropdown").val());
    fd.append("section_id", $("#section-dropdown").val());
    fd.append('user_id',document.getElementById('user_id').value)
    let url = '/workforce/manageemployee/import_employees/'

    //process_file
    process_file(url, fd);
    hideLoading()
}

//auto select checkbox
function auto_select_checkbox(element_id) {
    let element_value = document.getElementById(element_id).value;
    let element_name = element_id.split('--')[0].replace('-', ' ');
    let checkbox_element = document.getElementsByName(element_name + '--checkbox');
    checkbox_element.forEach(function (e, v) {
        if (element_value === '') {
            $('#'+e.id).click();
        } else {
            $('#'+e.id).click();

        }
    });
}

function display_details(matched, total) {
    document.getElementById("details").innerHTML = '';
    document.getElementById("details").innerHTML +=
        "<p align=center>( " + matched + "/" + total + " columns are selected )</p>";
}

function get_duplicated_selections() {
    let field_to_count_map = new Map();
    $("select[class*='section--']").each(function (i, v) {
        if (v.value != '') {
            if (field_to_count_map.has(v.value)) {
                field_to_count_map.set(v.value, field_to_count_map.get(v.value) + 1);
            } else {
                field_to_count_map.set(v.value, 1);
            }
        }
    });

    let duplicated_fields = [];
    field_to_count_map.forEach(function (v, k) {
        if (v > 1) {
            duplicated_fields.push(k)
        }
    });

    let duplication_paragraph = document.getElementById("duplication_details");
    if (duplicated_fields.length === 0) {
        duplication_paragraph.innerHTML = '';
    } else {

        duplication_paragraph.innerHTML = "( Duplicated entries : ";
        duplicated_fields.forEach(function (v, i) {
            duplication_paragraph.innerHTML += v + " ,";
        })
        duplication_paragraph.innerHTML += " )";

        duplication_paragraph.innerHTML = duplication_paragraph.innerHTML.replace(/,\s*\)$/, " )")
    }
}

