import { ZoneLimit } from '../../shared/shared'
import { formatDate } from '../../shared/utility'
import './fish-table.css'

interface FishTableProps {
    zoneLimits: ZoneLimit[]
}

function FishTable({ zoneLimits }: FishTableProps) {

    return (
        <table className='striped'> 
            <thead>
                <tr>
                    <th>Zone</th>
                    <th>Species</th>
                    <th>Season(s)</th>
                </tr>

            </thead>
            <tbody>
                {zoneLimits.map((zl, zlIndex) =>
                    zl.fishLimits.map((fl, flIndex) =>
                        fl.rangeLimits.map((rl, rlIndex) =>
                            <tr>
                                {(flIndex == 0 && rlIndex == 0) && <td className={zlIndex%2 == 0 ? 'dark-zone' : 'light-zone'} rowSpan={zl.fishLimits.reduce((total, p) => {return total + (p.rangeLimits.length || 0)}, 0)}>{zl.zoneNumber}</td>}
                                {(rlIndex == 0) && <td className={flIndex%2 == 0 ? 'dark-fish' : 'light-fish'} rowSpan={fl.rangeLimits.length}>{fl.species}</td>}
                                {(rl.startDate.getTime() == rl.endDate.getTime()) && <td>Closed all year</td>}
                                {(rl.startDate.getTime() != rl.endDate.getTime()) && <td>{formatDate(rl.startDate)} - {formatDate(rl.endDate)}</td>}
                            </tr>
                        )
                    )
                )}

            </tbody>
        </table>
    )
}

export default FishTable
