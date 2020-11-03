function searchEmpTbl(inputid, tableid, colno) {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById(inputid);
    filter = input.value.toUpperCase();
    table = document.getElementById(tableid);
    tr = table.getElementsByTagName("tr");
    var nd = -1;
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[colno];
        console.log("td:" + td);
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
                nd += 1;
            } else {
                tr[i].style.display = "none";
            }
        }
        if (nd === -1) {
            document.getElementById("no_data_table").style.display = "contents";
        } else {
            document.getElementById("no_data_table").style.display = "none";
        }
    }
}

function searchAllEmpTbl(inputid, tableid, colno) {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById(inputid);
    filter = input.value.toUpperCase();
    table = document.getElementById(tableid);
    tr = table.getElementsByTagName("tr");
    let nd = -1;
    for (let i = 0; i < tr.length; i++) {
        for (let j = 1; j < colno; j++) {

            td = tr[i].getElementsByTagName("td")[j];
            if (td) {
                txtValue = td.textContent || td.innerText;
                if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    tr[i].style.display = "";
                    nd += 1;
                    break
                } else {
                    tr[i].style.display = "none";
                }
            }
        }
        if (nd === -1) {
            document.getElementById("nodatarow").style.display = "contents";

        } else {

            document.getElementById("nodatarow").style.display = "none";
        }
    }

}


function searchByCol(inputid, tableid, colno) {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById(inputid);
    filter = input.value.toUpperCase();
    table = document.getElementById(tableid);
    tr = table.getElementsByTagName("tr");
    var nd = -1;
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[colno];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
                nd += 1;
            } else {
                tr[i].style.display = "none";
            }
        }
        if (nd === -1) {
            document.getElementById("nodatarow").style.display = "contents";
        } else {
            document.getElementById("nodatarow").style.display = "none";
        }
    }
}
