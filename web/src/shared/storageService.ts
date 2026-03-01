export class StorageService{
    static get ZoneLabels(): { [key: number]: string } {
        const zoneLabels: string | null =localStorage.getItem('zoneLabels');
        if(zoneLabels){
            return JSON.parse(zoneLabels);
        }
        else{
            return {};
        }
    }

    static set ZoneLabels(zoneLabels: {}) {
        localStorage.setItem('zoneLabels', JSON.stringify(zoneLabels))
    }
}