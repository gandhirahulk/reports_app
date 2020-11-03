$('#add_holiday_button').on('click', function () {
    if ($('#create_holiday').css('display') == 'none') {
        $('#create_holiday').css('display', 'block');
    } else {
        $('#create_holiday').css('display', 'none');
    }
});

$('.addroleclose').on('click', function () {
    $('#create_holiday').css('display', 'none');
});

$('#holiday_date').on('change', function () {

    let fd_fd = new FormData();
    fd_fd.append('holiday_date', document.getElementById('holiday_date').value)
    fd_fd.append('csrfmiddlewaretoken', csrf_token);
    $.ajax({
        url: 'fetch_day/',
        method: 'POST',
        data: fd_fd,
        dataType: 'json',
        contentType: false,
        processData: false,
        success: function (data) {
            if (data) {
                let day_map = {
                    0: 'Monday',
                    1: 'Tuesday',
                    2: 'Wednesday',
                    3: 'Thursday',
                    4: 'Friday',
                    5: 'Saturday',
                    6: 'Sunday'
                }
                document.getElementById('holiday_day').innerText = 'Day: ' + day_map[data['day']];
            } else {
                alert("ajax call not success.");
            }
        },
        fail: function () {
            alert('request failed');
        }
    })
})


