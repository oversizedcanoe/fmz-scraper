import jsonData from '../assets/2026.json';
import { FishLimit, RangeLimit, ZoneLimit } from './shared';

export function parseJsonToLimits(): ZoneLimit[]{
    const zoneLimits: ZoneLimit[] = []

    jsonData.forEach((zl) => {
        let zoneLimit: ZoneLimit = new ZoneLimit();
        zoneLimit.zoneNumber = zl.zone_number;

        let fishLimits: FishLimit[] = [];

        zl.fish_limits.forEach((fl) => {
            let fishLimit: FishLimit = new FishLimit();
            fishLimit.species = fl.species;

            let rangeLimits: RangeLimit[] = [];
            
            fl.limits.forEach((rl) => {
                let rangeLimit: RangeLimit = new RangeLimit();
                rangeLimit.startDate = new Date(rl.start_date);
                rangeLimit.endDate = new Date(rl.end_date);
                rangeLimits.push(rangeLimit);
            })

            fishLimit.rangeLimits = rangeLimits;
            fishLimits.push(fishLimit);
        })

        zoneLimit.fishLimits = fishLimits;
        zoneLimits.push(zoneLimit);
    })

    return zoneLimits;
}

export function formatDate(date: Date){
    const tempDateString = date.toUTCString().split(' 00')[0]
    return tempDateString.substring(0, tempDateString.length - 4);
}