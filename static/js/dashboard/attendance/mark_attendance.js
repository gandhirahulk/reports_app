function mark_attendance() {
    let fd_ma = new FormData();

    fd_ma.append('uid', document.getElementById('uid_input').value)
    fd_ma.append('img_link', document.getElementById('image_link').value)
    fd_ma.append('latitude', document.getElementById('latitude_input').value)
    fd_ma.append('longitude', document.getElementById('longitude_input').value)
    fd_ma.append('accuracy', document.getElementById('accuracy_input').value)
    fd_ma.append('sub_source', document.getElementById('sub_source_input').value)

    fd_ma.append('csrfmiddlewaretoken', csrf_token);
    $.ajax({
        url: 'attendance/',
        method: 'POST',
        data: fd_ma,
        dataType: 'json',
        contentType: false,
        processData: false,
        success: function (data) {
            if (data) {
                alert(data['attendance'])
            } else {
                alert("ajax call not success.");
            }
        },
        fail: function () {
            alert('request failed');
        }
    });
}