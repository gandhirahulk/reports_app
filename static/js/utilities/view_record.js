function view_record(element_pk) {
    const fd = new FormData();
    fd.append("csrfmiddlewaretoken", csrf_token);
    $.ajax({
        url: 'view/' + element_pk + '/',
        method: 'POST',
        data: fd,
        dataType: 'json',
        contentType: false,
        processData: false,
        success: function (data) {
            console.log(data)
            if (data) {
                document.getElementById('view_record').style.display = 'block';
                jQuery.each(data['basic_details'], function (key, value) {
                    document.getElementById('basic_details').innerHTML += '<label>' + key + value + '</label>';
                })

                jQuery.each(data['creation_details'], function (key, value) {
                    document.getElementById('creation_details').innerHTML += '<label>' + key + value + '</label>';
                })
            }
        },
        fail: function () {
            console.log('request failed');
        }
    });
    document.getElementById('view_record').style.display = 'block';
}

$('#view_close_button').on('click', function () {
    document.getElementById('view_record').style.display = 'none';
});