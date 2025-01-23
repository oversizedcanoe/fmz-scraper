import { useEffect, useState } from 'react';
import './App.css'
import Header from './components/header/header'
import UserControls from './components/user-controls/user-controls'
import { ZoneLimit } from './shared/shared';
import { parseJsonToLimits } from './shared/utility';
import FishTable from './components/fish-table/fish-table';

function App() {
  let emptyZoneLimits: ZoneLimit[] = [];
  const [zoneLimits, setZoneLimits] = useState(emptyZoneLimits);
  const [filteredZoneLimits, setFilteredZoneLimits] = useState(emptyZoneLimits);
  const [zoneNumberToFilter, setZoneNumberToFilter] = useState(0);
  const [showInSeasonOnly, setShowInSeasonOnly] = useState(false);

  useEffect(() => {
    const json = parseJsonToLimits();
    setZoneLimits(json);
    setFilteredZoneLimits(json);
  }, [])

  useEffect(() => {
    filterLimits();
  }, [showInSeasonOnly, zoneNumberToFilter, zoneLimits])

  function handleShowInSeasonOnlyChange(onlyInSeason: boolean) {
    setShowInSeasonOnly(onlyInSeason);
  }

  function handleZoneChange(zoneNumber: number) {
    console.warn('zone change = ', zoneNumber);
    setZoneNumberToFilter(zoneNumber);
  }

  function handleOnClearFilter(): void {
    setZoneNumberToFilter(0);
    setShowInSeasonOnly(false);
  }

  function filterLimits() {
    console.warn('filtering, zoneNumberToFilter=', zoneNumberToFilter, ' , showInSeasonOnly=',showInSeasonOnly)
    let limitsToShow = zoneLimits;

    if (zoneNumberToFilter != 0) {
      limitsToShow = limitsToShow.filter(zl => zl.zoneNumber == zoneNumberToFilter);
    }

    if (showInSeasonOnly) {
      const today: Date = new Date();
      limitsToShow = limitsToShow.map(zoneLimit => {
        return {
          ...zoneLimit,
          fishLimits: zoneLimit.fishLimits.map(fishLimit => {
            return {
              ...fishLimit,
              rangeLimits: fishLimit.rangeLimits.filter(rangeLimit => {
                return today >= new Date(rangeLimit.startDate) && today <= new Date(rangeLimit.endDate);
              })
            };
          }).filter(fishLimit => fishLimit.rangeLimits.length > 0) // Remove fish limits without valid range limits
        };
      }).filter(zoneLimit => zoneLimit.fishLimits.length > 0); // Remove zones without valid fish limits
      
    }

    setFilteredZoneLimits(limitsToShow);
  }

  return (
    <>
      <Header />
      <main className="container">
        <article>
          <UserControls onInSeasonChange={handleShowInSeasonOnlyChange} onZoneChange={handleZoneChange} onClearFilter={handleOnClearFilter} />
        </article>

        <article>
          <FishTable zoneLimits={filteredZoneLimits} />
        </article>
      </main>

    </>
  )
}

export default App
