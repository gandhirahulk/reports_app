$('.tabs_btn').on('click', function () {
    let fd_fo = new FormData();
    let field_name = this.textContent;
    let element_id = this.id;
    let table_div = $('#'+element_id+'_div');
    fd_fo.append('csrfmiddlewaretoken', csrf_token);
    $.ajax({
        url: field_name + '/',
        method: 'POST',
        data: fd_fo,
        dataType: 'text',
        contentType: false,
        processData: false,
        success: function (data) {
            if (data) {
                table_div.html(data)
            } else {
                alert("ajax call not success.");
            }
        },
        fail: function () {
            alert('request failed');
        }
    })
})