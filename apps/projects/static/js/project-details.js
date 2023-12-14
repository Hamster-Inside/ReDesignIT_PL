// project-details.js

function createLinkToSource(url, logoPath) {
    return url ? `
        <div class="div-link-to-source rounded-3 d-flex align-items-center">
            <a href="${url}" target="_blank">
                <img src="${logoPath}">
            </a>
        </div>
    ` : '';
}
function showProjectDetails(projectElement) {
    var name = projectElement.dataset.name;
    var summary = projectElement.dataset.summary;
    var imageUrl = projectElement.dataset.image;
    var githubUrl = projectElement.dataset.githubUrl;
    var githubLogoPath = projectElement.dataset.githubLogoPath;
    var youtubeUrl = projectElement.dataset.youtubeUrl;
    var youtubeLogoPath = projectElement.dataset.youtubeLogoPath;

    var githubLink = createLinkToSource(githubUrl, githubLogoPath);
    var youtubeLink = createLinkToSource(youtubeUrl, youtubeLogoPath);

    var detailsHtml = `
        <div class="div-project-detail">
            <div class="project-image">
                <img src="${imageUrl}">
            </div>
            <div class="project-title d-flex text-center justify-content-center align-items-center">
                <h4>${name}</h4>
            </div>
        </div>
        <div class="div-project-detail">
            <div class="div-connected-links align-items-center">
                ${githubLink}
                ${youtubeLink}
            </div>
            <div class="px-4">
                ${summary}
            </div>
        </div>
    `;

    document.getElementById('project-details').innerHTML = detailsHtml;
}
