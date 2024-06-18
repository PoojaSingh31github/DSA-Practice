console.log("square star pattern");
for (i = 1; i <= 5; i++) {
    let row = "";
    for (j = 1; j <= 5; j++) {
        row += i;
    }
    console.log(row);
}

console.log("left triangle pattern");
for (i = 1; i <= 5; i++) {
    let row = "";
    for (j = 1; j <= i; j++) {
        row += i;
    }
    console.log(row);
}
console.log("right triangle pattern");
for (let i = 1; i <= 5; i++) {
    let row = "";
    for (let j = 0; j <= 4 - i; j++) {
        row += ' '
    }
    for (let k = 0; k < i; k++) {
        row += k;
    }
    console.log(row);
}
console.log("downside triangle pattern");
for (i = 1; i <= 5; i++) {
    let row = "";
    for (j = 5; j >= i; j--) {
        row += i;
    }
    console.log(row);
}
console.log("hollow sqaure pattern");
let row = "";
for (let i = 0; i < 5; i++) {
    row = "";
    for (let j = 0; j < 5; j++) {
        if (i == 0 || i == 4) {
            row += "*";
        } else if (j == 0 || j == 4) {
            row += "*";
        } else {
            row += " ";
        }
    }
    console.log(row);
}

console.log("Hollow triangle pattern");
for (let i = 1; i <= 5; i++) {
    let row = "";
    for (let j = 0; j < i; j++) {
        if (i == 5) {
            row += "*";
        } else if (j == 0 || j == i - 1) {
            row += "*";
        } else {
            row += " ";
        }
    }
    console.log(row);
}
console.log("Javascript Pyramid pattern");
for (let i = 1; i <= 5; i++) {
    let row = "";
    for (let j = 5; j >= i; j--) {
        row += " ";
    }
    for (let k = 0; k < 2 * (i - 1) + 1; k++) {
        row += "*";
    }
    console.log(row);
}
console.log("Reversed Pyramid Star pattern");
for (let i = 0; i < 5; i++) {
    let row = "";
    for (let j = 0; j < i; j++) {
        row += " ";
    }
    for (let k = 0; k < 2 * (5 - i) - 1; k++) {
        row += "*";
    }
    console.log(row);
}
console.log("Hollow Pyramid star pattern");
for (let i = 1; i <= 5; i++) {
    let row = "";
    for (let j = 1; j <= 5 - i; j++) {
        row += " ";
    }
    for (let k = 0; k < 2 * i - 1; k++) {
        if (i == 0 || i == 5) {
            row += "*";
        } else if (k == 0 || k == 2 * i - 2) {
            row += "*";
        } else {
            row += " ";
        }
    }
    console.log(row);
}

console.log("Diamond Pattern star pattern");
for (let i = 1; i <= 5; i++) {
    let row = "";
    for (let j = 1; j <= 5 - i; j++) {
        row += " ";
    }
    for (let k = 0; k < 2 * i - 1; k++) {
        row += "*";
    }
    console.log(row);
} for (let i = 1; i < 5; i++) {
    let row = "";
    for (let j = 0; j < i; j++) {
        row += " ";
    }
    for (let k = 0; k < 2 * (5 - i) - 1; k++) {
        row += "*";
    }
    console.log(row);
}
console.log("hourglass star pattern");
for (let i = 0; i < 5; i++) {
    let row = '';
    for (let j = 0; j < i; j++) {
        row += ' ';
    }
    for (let k = 0; k < (5 - i) * 2 - 1; k++) {
        row += '*';
    }
    console.log(row);
}

// Lower half of hourglass
for (let i = 2; i <= 5; i++) {
    let row = '';
    for (let j = 0; j < 5 - i; j++) {
        row += ' ';
    }
    for (let k = 0; k < i * 2 - 1; k++) {
        row += '*';
    }
    console.log(row);
}
console.log("Right Pascal star pattern");
for (let i = 1; i <= 5; i++) {
    let row = '';
    
    // Print spaces to align the pattern to the right
    for (let j = 0; j < 5 - i; j++) {
        row += ' ';
    }

    // Print stars for the current row
    for (let j = 0; j < i; j++) {
        row += '*';
    }
    
    console.log(row);
}
