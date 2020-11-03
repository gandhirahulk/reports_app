$('#render_table').on('click', function () {
    let start_date = document.getElementById('start_date').value;
    let end_date = document.getElementById('end_date').value;
    if (start_date !== null && end_date !== null) {
        let fd_fa = new FormData();
        fd_fa.append('start_date', start_date)
        fd_fa.append('end_date', end_date)
        fd_fa.append('csrfmiddlewaretoken', csrf_token);
        $.ajax({
            url: '/self_service/team/team_attendance/fetch_attendance',
            method: 'POST',
            data: fd_fa,
            dataType: 'json',
            contentType: false,
            processData: false,
            success: function (data) {
                if (data) {

                    let headings_element_row = document.getElementById('headings');
                    $("#headings th").each(function (i,heading_element) {
                        if(i>=2){
                            heading_element.remove();
                        }
                    })

                    for (let index = 0; index < data['interval'].length; index++) {
                        headings_element_row.innerHTML += "<th>" + data['interval'][index] + "</th>";
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
});
