const fs = require('fs');

let md = fs.readFileSync('partie_6_couts_shoploc.md', 'utf8');

// Replace codecogs URLs with non-accented text to avoid image rendering issues
md = md.replace(/text\{Co%C3%BBt/g, 'text{Cout');
md = md.replace(/text\{R%C3%A9sultat/g, 'text{Resultat');
// And just in case for any other occurrences
md = md.replace(/Co%C3%BBt/g, 'Cout');
md = md.replace(/R%C3%A9sultat/g, 'Resultat');

fs.writeFileSync('partie_6_couts_shoploc.md', md, 'utf8');
console.log('Markdown URLs updated.');
