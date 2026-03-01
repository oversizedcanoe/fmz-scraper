import { useState } from 'react';
import { StorageService } from '../../shared/storageService';
import './user-controls.css'

interface UserControlsProps {
  onZoneChange: Function;
  onInSeasonChange: Function;
  onFilterClear: Function;
}

function UserControls({ onZoneChange, onInSeasonChange, onFilterClear }: UserControlsProps) {
  const [zoneNumberToFilter, setZoneNumberToFilter] = useState(0);
  const [showInSeasonOnly, setShowInSeasonOnly] = useState(false);
  const [zoneLabels, setZoneLabels] = useState(StorageService.ZoneLabels || {});
  const zoneQuantity = 20;

  function onShowInSeasonOnlyChecked() {
    const newValue = !showInSeasonOnly;
    setShowInSeasonOnly(newValue);
    onInSeasonChange(newValue);
  }

  function onZoneDropdownChanged(zoneNumber: any) {
    setZoneNumberToFilter(zoneNumber);
    onZoneChange(zoneNumber)
  }

  function onClearFilterClicked() {
    setShowInSeasonOnly(false);
    setZoneNumberToFilter(0);
    onFilterClear();
  }

  function onLabelZoneClicked(zoneNumber: number) {
    const label: string | null = prompt(`What would you like to label Zone ${zoneNumber}?`)

    const newLabels = {
      ...zoneLabels,
      [zoneNumber]: label ?? ""
    };

    setZoneLabels(newLabels);
    StorageService.ZoneLabels = newLabels;
  }

  return (
    <form>
      <fieldset className="grid">
        <div>
          <select name="zoneNumber" value={zoneNumberToFilter} onChange={(e) => onZoneDropdownChanged(e.target.value)}>

            <option value={0}>All Zones</option>
            {Array.from({ length: zoneQuantity }, (_, i) => {
              const zone = i + 1;
              const label = zoneLabels?.[zone];

              return (
                <option value={zone} key={zone}>
                  Zone {zone}{label ? ` (${label})` : ""}
                </option>
              );
            })}

          </select>
          <a href="https://www.ontario.ca/fishonline" target="_blank">Find your Zone</a>
        </div>
        <label>
          <input type="checkbox" name="notify" checked={showInSeasonOnly} onChange={onShowInSeasonOnlyChecked} />
          In Season Only
        </label>

        {zoneNumberToFilter > 0 && <button type="button" onClick={() => onLabelZoneClicked(zoneNumberToFilter)}>Label Zone</button>}

        <button onClick={onClearFilterClicked} type='reset'>Clear Filter</button>

      </fieldset>
    </form>
  )
}

export default UserControls




