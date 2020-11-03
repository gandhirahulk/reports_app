function fetch_attendance_details() {
    let fd_ad = new FormData();
    fd_ad.append('uid', document.getElementById('uid_input').value)
    fd_ad.append('csrfmiddlewaretoken', csrf_token);
    $.ajax({
        url: 'attendance/fetch_attendance_details/',
        method: 'POST',
        data: fd_ad,
        dataType: 'json',
        contentType: false,
        processData: false,
        success: function (data) {
            if (data) {
                document.getElementById('in_time').innerText = 'In Time: ' + data['in_time'];
                document.getElementById('out_time').innerText = 'Out Time: ' + data['out_time'];
                document.getElementById('total_hours').innerText = 'Total Hours: ' + data['total_hours']
            } else {
                alert("ajax call not success.");
            }
        },
        fail: function () {
            alert('request failed');
        }
    })
}

