function downloadPDF() {
    const name = document.querySelector('.profile-header h1').textContent.trim().replace(/\s+/g, '_');
    const date = new Date().toISOString().split('T')[0];
    const originalTitle = document.title;
    const newTitle = `${name}_${date}`;

    document.title = newTitle;

    // Give the browser time to update the title before opening print dialog
    setTimeout(() => {
        window.print();
        // Restore original title after print dialog closes
        setTimeout(() => { document.title = originalTitle; }, 100);
    }, 100);
}
