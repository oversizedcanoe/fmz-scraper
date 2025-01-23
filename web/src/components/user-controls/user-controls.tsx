import { useState } from 'react';

interface UserControlsProps {
  onZoneChange: Function;
  onInSeasonChange: Function;
  onClearFilter: Function;
}

function UserControls({onZoneChange, onInSeasonChange, onClearFilter}: UserControlsProps) {
  const [showInSeasonOnly,setShowInSeasonOnly] = useState(false);
  const zoneQuantity = 20;

  function onShowInSeasonOnlyChecked(){
    const newValue = !showInSeasonOnly;
    setShowInSeasonOnly(newValue);
    onInSeasonChange(newValue);
  }

  return (
    <form>
    <fieldset className="grid">
        <select name="zoneNumber" onChange={(e) => onZoneChange(e.target.value)}>

          <option value={0}>All Zones</option>
          {[...Array(zoneQuantity)].map((_, i) =>
                <option value={i+1} key={i}>Zone {i+1}</option>
          )}

        </select>
      <label>
        <input type="checkbox" name="notify" checked={showInSeasonOnly} onChange={() => onShowInSeasonOnlyChecked()} />
        In Season Only
      </label>

      <button onClick={() => onClearFilter()} type='button'>Clear Filter</button>
    </fieldset>
  </form>
  )
}

export default UserControls




 