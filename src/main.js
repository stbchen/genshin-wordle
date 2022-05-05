// Genshin Guessle
'use strict';

let config = {
    type: Phaser.CANVAS,
    width: 1080,
    height: 720,
    scene: [Genshinguessle],
};

let cursors;

let game = new Phaser.Game(config);