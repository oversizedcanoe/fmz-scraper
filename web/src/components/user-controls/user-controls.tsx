import { useState } from 'react';

interface UserControlsProps {
  onZoneChange: Function;
  onInSeasonChange: Function;
  onFilterClear: Function;
}

function UserControls({onZoneChange, onInSeasonChange, onFilterClear}: UserControlsProps) {
  const [zoneNumberToFilter, setZoneNumberToFilter] = useState(0);
  const [showInSeasonOnly,setShowInSeasonOnly] = useState(false);
  const zoneQuantity = 20;

  function onShowInSeasonOnlyChecked(){
    const newValue = !showInSeasonOnly;
    setShowInSeasonOnly(newValue);
    onInSeasonChange(newValue);
  }

  function onZoneDropdownChanged(zoneNumber: any){
    setZoneNumberToFilter(zoneNumber);
    onZoneChange(zoneNumber)
  }

  function onClearFilterClicked(){
    setShowInSeasonOnly(false);
    setZoneNumberToFilter(0);
    onFilterClear();
  }

  return (
    <form>
    <fieldset className="grid">
        <select name="zoneNumber" value={zoneNumberToFilter} onChange={(e) => onZoneDropdownChanged(e.target.value)}>

          <option value={0}>All Zones</option>
          {[...Array(zoneQuantity)].map((_, i) =>
                <option value={i+1} key={i}>Zone {i+1}</option>
          )}

        </select>
      <label>
        <input type="checkbox" name="notify" checked={showInSeasonOnly} onChange={onShowInSeasonOnlyChecked} />
        In Season Only
      </label>

      <button onClick={onClearFilterClicked} type='button'>Clear Filter</button>
    </fieldset>
  </form>
  )
}

export default UserControls




 