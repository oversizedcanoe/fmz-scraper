// Dictionary where the key is the zone number and value is the number of sub rows it contains
let zoneNumberAndRowCount = {};

window.onload = function () {
    initializeZoneNumberAndRowCount();
    intializeDropdown();
    initializeInSeasonToggle();
    initializeResetButton();
}

function initializeZoneNumberAndRowCount() {
    const zoneRows = document.querySelectorAll("tbody>tr.zoneRow");

    for (let i = 0; i < zoneRows.length; i++) {
        const zoneRow = zoneRows[i];
        const zoneNumber = i + 1;
        const subRowCount = zoneRow.firstElementChild.getAttribute('rowspan');
        zoneNumberAndRowCount[zoneNumber] = Number(subRowCount);
    }
}

function intializeDropdown() {
    const zoneCheckboxes = document.getElementsByClassName("zoneCheckbox");

    for (let i = 0; i < zoneCheckboxes.length; i++) {
        let zoneCheckbox = zoneCheckboxes[i]
        zoneCheckbox.addEventListener("click", function () {
            handleZoneToggled(i, zoneCheckbox.checked)
        })
    }
}

function initializeInSeasonToggle() {

}

function initializeResetButton() {

}

function handleZoneToggled(zoneNumber, showZone){
    const zoneCheckboxes = document.querySelectorAll(".zoneCheckbox");
    const quantityCheckedZones = Array.from(zoneCheckboxes).filter(zc => zc.checked == true).length;
    const allZonesChecked = zoneNumber == 0;

    if (showZone){
        if(allZonesChecked){
            // uncheck all other zones
            for (let i = 1; i < zoneCheckboxes.length; i++) {
                zoneCheckboxes[i].checked = false;
            }
        } 
        else {
            // specific zone has been toggled
            // uncheck "All Zones"
            zoneCheckboxes[0].checked = false;
        }
    }
    else {
        // we are unchecking a zone/option
        if (quantityCheckedZones == 0) {
            // if no zone is checked, keep "All Zones" checked
            zoneCheckboxes[0].checked = true;
        }
    }
    updateRowVisibility();
}


function updateRowVisibility() {
    let hiddenZoneNumbers = []
    const zoneCheckboxes = document.getElementsByClassName("zoneCheckbox");

    // only append to hiddenZoneNumbers if "AllZones" not checked
    if (zoneCheckboxes[0].checked == false){
        for (let i = 1; i < zoneCheckboxes.length; i++) {
            if (zoneCheckboxes[i].checked == false) {
                hiddenZoneNumbers.push(i);
            }
        }
    }

    const tableRows = document.querySelectorAll("tr");
    let rowNumber = 0;

    for (const zoneNumber in zoneNumberAndRowCount) {
        for(let subIndex = 1; subIndex < zoneNumberAndRowCount[zoneNumber] + 1; subIndex++) {
            if (hiddenZoneNumbers.indexOf(Number(zoneNumber)) > -1) {
                tableRows[rowNumber].classList.add("hidden")
            } else {
                tableRows[rowNumber].classList.remove("hidden")
            }

            rowNumber++
        }
    }
}