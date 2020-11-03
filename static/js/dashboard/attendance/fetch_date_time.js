function fetch_date_time() {
    let fd_dt = new FormData();
    fd_dt.append('csrfmiddlewaretoken', csrf_token);
    $.ajax({
        url: 'utilities/fetch_date_time',
        method: 'POST',
        data: fd_dt,
        dataType: 'json',
        contentType: false,
        processData: false,
        success: function (data) {
            if (data) {
                document.getElementById('date').innerText = data['date'];
                document.getElementById('time').innerText = data['time'];
            } else {
                alert("ajax call not success.");
            }
        },
        fail: function () {
            alert('request failed');
        }
    });
}

