// select all
$(document).ready(function () {
    $("#selectallemp").on("click", function () {
        if (this.checked) {
            empcheckboxes = document.getElementsByName('empselect');
            for (var i = 0, n = empcheckboxes.length; i < n; i++) {
                empcheckboxes[i].checked = true;
            }
        } else {
            empcheckboxes = document.getElementsByName('empselect');
            for (var i = 0, n = empcheckboxes.length; i < n; i++) {
                empcheckboxes[i].checked = false;
            }
        }
    });
    $(".eachempselect").on("click", function () {
        allcheckboxes = document.getElementsByName('empselect');
        if (this.checked) {
            var checked = 0;
            for (var i = 0, n = allcheckboxes.length; i < n; i++) {
                if (allcheckboxes[i].checked == true) {
                    checked += 1;
                }
            }
            if (checked === n) {
                selectallcheckbox = document.getElementById('selectallemp');
                selectallcheckbox.checked = true;
            }
        } else {
            selectallcheckbox = document.getElementById('selectallemp');
            selectallcheckbox.checked = false;
        }
    });
});

//filter
function showTr() {
    document.getElementById('search-emp-tbl').classList.toggle('showtr');
}

function showFilterWindow() {
    document.getElementById("drawer-content").classList.toggle("withfilter-drawer-content"); //working
    document.getElementById("Manageemployee").classList.toggle("withfilter-tab-content-block");
}