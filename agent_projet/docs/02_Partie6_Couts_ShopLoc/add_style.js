const fs = require('fs');

const htmlContent = fs.readFileSync('partie_6_couts_shoploc.html', 'utf8');

const styledHtml = `<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; line-height: 1.6; }
        table { width: 100%; border-collapse: collapse; margin-bottom: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        h1, h2, h3 { color: #333; }
        img { max-width: 100%; }
        .center { text-align: center; }
    </style>
</head>
<body>
${htmlContent}
</body>
</html>`;

fs.writeFileSync('partie_6_couts_shoploc.html', styledHtml, 'utf8');
console.log('HTML styled and UTF-8 meta added.');
