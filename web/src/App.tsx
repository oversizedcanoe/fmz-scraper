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

  useEffect(() =>{
    setZoneLimits(parseJsonToLimits());
  }, [])



  function handleShowInSeasonOnlyChange(showInSeasonOnly: boolean){
    console.log(showInSeasonOnly);
  }

  function handleZoneChange(zoneNumber: number){
    console.log(zoneNumber);
  }

  return (
    <>
      <Header />
      <main className="container">

        <article>
        <UserControls onInSeasonChange={handleShowInSeasonOnlyChange} onZoneChange={handleZoneChange} /> 
        </article>

        <article>
          <FishTable zoneLimits={zoneLimits} />
        </article>
      </main>

    </>
  )
}

export default App
