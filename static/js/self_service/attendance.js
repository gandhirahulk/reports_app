let userId = document.getElementById('user-id').textContent;
userId = userId.replace('Logout', "");
userId = userId.replace('[', "");
userId = userId.replace(']', "");
userId = userId.replace(" ", '');

$('#render_table').on('click', function () {
    document.getElementsByClassName('table-wrapper-div')[1].style.display = 'block';
    let fd_ad = new FormData();
    fd_ad.append('uid', userId.trim())
    fd_ad.append('payroll_month', document.getElementById('payroll_month').value)
    fd_ad.append('csrfmiddlewaretoken', csrf_token);
    $.ajax({
        url: '/self_service/attendance/U2345/fetch_attendance/',
        method: 'POST',
        data: fd_ad,
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
                let input_data = document.getElementById('input_data');
                $("#input_data tr").each(function (i, details) {
                    if (i >= 1) {
                        details.remove();
                    }
                })

                let start_day = data['start_day']
                for (let index = 0; index < data['interval'].length; index++) {
                    let record_date = data['interval'][index]
                    let initiate_row = '<tr><td><input id="' + record_date + '" onclick="get_details(this.id)" class="attendance_expand" type="button" value="+/-"></td>';
                    let dates = '<td>' + record_date + "</td>";
                    let day = '<td>' + day_map[(start_day + index) % 7] + '</td>';
                    let name = '<td>' + 'name' + '</td>';
                    let type = '<td>' + 'type' + '</td>';
                    let start_time = '<td>' + 'start_time' + '</td>';
                    let end_time = '<td>' + 'shift_end_time' + '</td>';
                    let in_time = '<td>' + data['in_time'][index] + '</td>';
                    let out_time = '<td>' + data['out_time'][index] + '</td>';
                    let total_hours = '<td>' + data['total_hours'][index] + '</td>';
                    let status = '<td>' + 'status' + '</td>';
                    let remark = '<td>' + 'remark' + '</td>';


                    input_data.innerHTML += initiate_row + dates + day + name + type + start_time + end_time + in_time + out_time + total_hours + status + remark + '</tr>';
                }
            } else {
                alert("ajax call not success.");
            }
        },
        fail: function () {
            alert('request failed');
        }
    })

})

function get_details(record_date) {
    $('#attendance_detail_form').css('display', 'block');
    let fd_ad = new FormData();
    fd_ad.append('uid', userId.trim())
    fd_ad.append('record_date', record_date)
    fd_ad.append('csrfmiddlewaretoken', csrf_token);
    $.ajax({
        url: '/self_service/attendance/U2345/fetch_day_details/',
        method: 'POST',
        data: fd_ad,
        dataType: 'json',
        contentType: false,
        processData: false,
        success: function (data) {
            if (data) {

                let input_data = document.getElementById('day_detail_input');
                $("#day_detail_input tr").each(function (i, details) {
                    details.remove();
                })

                for (let index = 0; index < data['time'].length; index++) {
                    let initiate_row = '<tr><td>' + data['time'][index] + '</td>';
                    let location = '<td><a href="" >' + data['location'][index] + "</a></td>";
                    let photo = '<td><a target="_blank" href="' + data['photo_link'][index] + '">View Image</a></td>';
                    let status = '<td>' + 'status' + '</td>';
                    let remark = '<td>' + 'remark' + '</td>';

                    input_data.innerHTML += initiate_row + location + photo + status + remark + '</tr>';
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

