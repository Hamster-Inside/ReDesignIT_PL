// project-details.js

function createLinkToSource(url, logoPath) {
    return url ? `
        <div class="div-link-to-source rounded-3 d-flex mx-auto align-items-center justify-content-center">
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

        <div class="row align-items-center">
            <div class="project-detail-img col-lg-4 col-12 order-lg-1 order-1 p-2 justify-content-center align-items-center">
                <img class="rounded-3" src="${imageUrl}">
            </div>
            <div class="col-lg-6 col-12 order-lg-2 order-2 mx-auto">
                <h4 class="text-center">${name}</h4>
            </div>
        </div>
        <div class="row">
            <div class="project-detail-links col-lg-4 col-12 order-lg-3 order-3 align-items-center">
                ${githubLink}
                ${youtubeLink}
            </div>
            <div class="col-lg-6 col-12 order-lg-4 order-4 px-4">
                ${summary}
            </div>
        </div>


    `;

    document.getElementById('project-details').innerHTML = detailsHtml;
}
