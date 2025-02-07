import './footer.css'

function Footer() {

    return (
        <footer>
            <div className='container'>
                <p className='left'>Always consult the <a href="https://www.ontario.ca/page/ontario-fishery-regulations-variation-orders">FMZ Website</a> to verify dates and species limits.</p>
                <p className='right'>View the <a href="https://github.com/oversizedcanoe/fmz-scraper">source</a> for this website.</p>
            </div>
        </footer>
    )
}

export default Footer
