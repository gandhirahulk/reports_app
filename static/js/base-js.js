function rotateArrow(m, toshowmenu) {
    if (document.getElementById(toshowmenu).classList[1] == "hidelist") {
        var x = document.getElementsByClassName("showlist");
        var y = document.getElementsByClassName("fa-chevron-up");
        for (i = 0; i < x.length; i++) {
            x[i].classList.remove("showlist");
        }
        for (i = 0; i < y.length; i++) {
            y[i].classList.toggle("fa-chevron-up");
        }
        document.getElementById(toshowmenu).classList.remove("hidelist");
        document.getElementById(toshowmenu).classList.add("showlist");
        var arrow = document.getElementById(m);
        arrow.classList.toggle("fa-chevron-up");
    } else {
        document.getElementById(toshowmenu).classList.remove("showlist");
        document.getElementById(toshowmenu).classList.add("hidelist");
        var x = document.getElementsByClassName("showlist");
        for (i = 0; i < x.length; i++) {
            x[i].classList.remove("showlist");
            x[i].classList.add("hidelist");
        }
        var arrow = document.getElementById(m);
        arrow.classList.toggle("fa-chevron-up");
    }
}

function rotateSubArrow(m, toshowmenu, n) {
    if (document.getElementById(toshowmenu).classList[1] == "hidesublist") {
        var x = document.getElementsByClassName("showsublist");
        var y = document.getElementsByClassName("fa-chevron-up");
        for (i = 0; i < x.length; i++) {
            x[i].classList.remove("showsublist");
        }
        for (i = 0; i < y.length; i++) {
            y[i].classList.toggle("fa-chevron-up");
        }
        document.getElementById(toshowmenu).classList.remove("hidesublist");
        document.getElementById(toshowmenu).classList.add("showsublist");
        var arrow = document.getElementById(m);
        arrow.classList.toggle("fa-chevron-up");
        console.log("if()");
    } else {
        document.getElementById(toshowmenu).classList.remove("showsublist");
        document.getElementById(toshowmenu).classList.add("hidesublist");
        var x = document.getElementsByClassName("showsublist");
        for (i = 0; i < x.length; i++) {
            x[i].classList.remove("showsublist");
            x[i].classList.add("hidesublist");
        }
        var arrow = document.getElementById(m);
        arrow.classList.toggle("fa-chevron-up");
        console.log("else()");
    }
}

function showMenu(toshowmenu, torotatearrow, selectedmenu) {
    wrap = document.getElementById("wrapper");
    if (wrap.classList[1] == "collapse") {
        wrap.classList.toggle("collapse");
    }

    var i;
    var x = document.getElementsByClassName("sidebarmenuitem");
    for (i = 0; i < x.length; i++) {
        x[i].classList.add("hidelist");
    }
    rotateArrow(torotatearrow, toshowmenu);
}

function showSubMenu(toshowsubmenu, torotatesubarrow, selectedarrow) {
    var i;
    var x = document.getElementsByClassName("sidebarsubmenuitem");
    for (i = 0; i < x.length; i++) {
        x[i].classList.add("hidesublist");
    }
    rotateSubArrow(torotatesubarrow, toshowsubmenu, selectedarrow);
}

function openTab(tab, activetab) {
    
    var i;
    var x = document.getElementsByClassName("tabs");
    var y = document.getElementsByClassName("tabs_btn");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
        y[i].classList.remove("active_tab");
    }
    document.getElementById(tab).style.display = "block";
    document.getElementById(activetab).classList.add("active_tab")
    sessionStorage.setItem("current_tab", tab)
    sessionStorage.setItem("current_tab_id", activetab)
    
}

function openSubTab(tab, activetab) {
    var i;
    var x = document.getElementsByClassName("subtabs");
    var y = document.getElementsByClassName("subtabs_btn");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
        y[i].classList.remove("active_tab");
    }
    document.getElementById(tab).style.display = "block";
    document.getElementById(activetab).classList.add("active_tab")
    sessionStorage.setItem("current_sub_tab", tab)
    sessionStorage.setItem("current_sub_tab_id", activetab)
}


function openSection(section, activesection) {
    var i;
    var x = document.getElementsByClassName("sections");
    var y = document.getElementsByClassName("sections_btn");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
        y[i].classList.remove("active_section");
    }
    try {
        document.getElementById(section).classList.toggle("showsection");
        document.getElementById(activesection).classList.toggle("active_section")
        sessionStorage.setItem("current_section", section)
        sessionStorage.setItem("current_section_id", activesection)
    } catch (TypeError) {
        console.log('caught error');
    }

}


function get_data_for_delete(selectedid, requestfrom, toshowmodal) {
    console.log(requestfrom)
    if (requestfrom === 'company') {
        $('#sidebar').css('z-index', -1);
        $('#' + toshowmodal).css('display', "block");
        var url = "http://127.0.0.1:8000/settings/organization/delete/" + selectedid;
        $('#deleteurl').attr('href', url);
    }
    if (requestfrom === 'vendor') {
        $('#sidebar').css('z-index', -1);
        $('#' + toshowmodal).css('display', "block");
        var url = "http://127.0.0.1:8000/settings/organization/vendordelete/" + selectedid;
        $('#deletevendorurl').attr('href', url);
    }
    if (requestfrom === 'business') {
        $('#sidebar').css('z-index', -1);
        $('#' + toshowmodal).css('display', "block");
        var url = "http://127.0.0.1:8000/settings/organization/businessdelete/" + selectedid;
        $('#deletebusinessurl').attr('href', url);
    }
}


function showDatalist(inputid, listid, newlistid) {
    var datalist_input = document.getElementById(inputid);
    var toshow_datalist = document.getElementById(listid);
    if (datalist_input.value.length >= 1) {
        toshow_datalist.setAttribute("id", newlistid);
    } else {
        toshow_datalist.setAttribute("id", "");
    }
    if (datalist_input.value === '') {
        toshow_datalist.setAttribute("id", "");
    }

}

function hide_previous_emp(element_id) {
    $('.search-emp-contents').each(function () {
        if (this.id != element_id) {
            $(this).css("display", "none");
        }
    });
    $('#search-emp-panel').css('display', 'block');
}
