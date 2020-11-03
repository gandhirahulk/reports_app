$('#render_table').on('click', function () {
    document.getElementsByClassName('table-wrapper-div')[1].style.display = 'block';
    let fd_ad = new FormData();
    fd_ad.append('uid', document.getElementById('emp_select').value.split('|')[0].trim())
    fd_ad.append('payroll_month', document.getElementById('payroll_month').value)
    fd_ad.append('csrfmiddlewaretoken', csrf_token);
    $.ajax({
        url: '/self_service/team/team_attendance/fetch_report/',
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
                    let first_half = '<td>' + 'first half status' + '</td>';
                    let second_half = '<td>' + 'second half status' + '</td>';
                    let day_status = '<td>' + 'status' + '</td>';
                    let remark = '<td>' + 'remark' + '</td>';

                    input_data.innerHTML += initiate_row + dates + day + name + type + start_time + end_time + in_time + out_time + total_hours + first_half + second_half + day_status + remark + '</tr>';
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