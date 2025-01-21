export class ZoneLimit {
    zoneNumber: number = 0;
    fishLimits: FishLimit[] = [];
}

export class FishLimit {
    species: string = ''
    rangeLimits: RangeLimit[] = [];
}

export class RangeLimit {
    startDate: Date = new Date();
    endDate: Date = new Date();
}