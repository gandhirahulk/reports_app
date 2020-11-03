function delete_record(selected_id) {
    $('#sidebar').css('z-index', -1);
    $('#delete_record').css('display', "block");
    let url = "delete/" + selected_id + '/';
    $('#delete_link').attr('href', url);
    document.getElementById('delete_record').style.display = 'block';
}


$('#delete_close_button').on('click', function () {
    document.getElementById('delete_record').style.display = 'none';
});
