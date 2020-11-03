document.getElementById('select_all').onclick = function () {
    var checkboxes = document.getElementsByClassName('all_emp');
    for (var checkbox of checkboxes) {
        if (checkbox.style.display != 'none') {
            checkbox.checked = this.checked;
        }
    }
}

$('.all_emp').on('click', function () {
    let total = 0;
    let checked = 0;
    var checkboxes = document.getElementsByClassName('all_emp');
    for (var checkbox of checkboxes) {
        if (checkbox.checked === true) {
            checked += 1;
        }
        total += 1;
    }
    if (checked === 0) {
        $('#select_all').prop({indeterminate: false});
        $('#select_all').prop({checked: false});
    } else if (checked !== total) {
        $('#select_all').prop({indeterminate: true});
    } else {
        $('#select_all').prop({indeterminate: false});
        $('#select_all').prop({checked: true});
    }

});
