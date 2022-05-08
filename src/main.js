// Genshin Guessle
'use strict';

let config = {
    type: Phaser.CANVAS,
    width: 1500,
    height: 720,
    scene: [Genshinguessle],
};
let borderUILength = config.width;
let keyY, keyTAB;

let game = new Phaser.Game(config);