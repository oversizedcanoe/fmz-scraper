import { ZoneLimit } from '../../shared/shared'
import './fish-table.css'

interface FishTableProps {
    zoneLimits: ZoneLimit[]
}

function FishTable({zoneLimits} : FishTableProps) {

    return (
        <table className="striped">
                <thead>
                    <tr>
                        <th>Zone</th>
                        <th>Species</th>
                        <th>Season(s)</th>
                    </tr>

                </thead>
                <tbody>
                    {zoneLimits.map((zl) => 
                        zl.fishLimits.map((fl) =>
                            fl.rangeLimits.map((rl) => 
                                <>
                                <tr>
                                <td>{zl.zoneNumber}</td>
                                <td>{fl.species}</td>
                                <td>{rl.startDate.toString()} - {rl.endDate.toString()}</td>
                                </tr>
                                </>
                            )
                        )
                    )}

                </tbody>
            </table>
    )
}

export default FishTable
