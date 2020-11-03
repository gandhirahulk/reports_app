$('#add_rule_button').on('click',function () {
    if($('#add_attendance_form').css('display') == 'none'){
    $('#add_attendance_form').css('display','block');}
    else{
        $('#add_attendance_form').css('display','none');
    }
});

$('.addroleclose').on('click',function () {
    $('#add_attendance_form').css('display','none');
});