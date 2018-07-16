const typeGroupMusic = function(musicians) {

    if (musicians <= 0) {
        return "not a group";
    }
    if (musicians === 1) {
        return "solo";
    }
    if (musicians === 2) {
        return "duet";
    }
    if (musicians === 3) {
        return "trio";
    }
    if (musicians === 4) {
        return "quartet";
    }
    if (musicians > 4) {
        return "this is a large group";
    }

}

for (let i = -1; i <= 5; i++) {
    console.log(typeGroupMusic(i));
}
