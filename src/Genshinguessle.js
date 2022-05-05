class Genshinguessle extends Phaser.Scene {
    constructor() {
        super("Genshinguessle");
    }
    create() {
        this.characters = new Map();
        this.characters.set("albedo", {weapon: "sword", vision: "geo", nation: "mondstadt"});
        this.characters.set("aloy", {weapon: "bow", vision: "cryo", nation: "collab"});
        this.characters.set("amber", {weapon: "bow", vision: "pyro", nation: "mondstadt"});
        this.characters.set("arataki itto", {weapon: "claymore", vision: "geo", nation: "inazuma"});
        this.characters.set("barbara", {weapon: "catalyst", vision: "hydro", nation: "mondstadt"});
        this.characters.set("beidou", {weapon: "claymore", vision: "electro", nation: "liyue"});
        this.characters.set("bennett", {weapon: "sword", vision: "pyro", nation: "mondstadt"});
        this.characters.set("chongyun", {weapon: "claymore", vision: "cryo", nation: "liyue"});
        this.characters.set("diluc", {weapon: "claymore", vision: "pyro", nation: "mondstadt"});
        this.characters.set("diona", {weapon: "bow", vision: "cryo", nation: "mondstadt"});
        this.characters.set("eula", {weapon: "claymore", vision: "cryo", nation: "mondstadt"});
        this.characters.set("fischl", {weapon: "bow", vision: "electro", nation: "mondstadt"});
        this.characters.set("ganyu", {weapon: "bow", vision: "cryo", nation: "liyue"});
        this.characters.set("gorou", {weapon: "bow", vision: "geo", nation: "inazuma"});
        this.characters.set("hu tao", {weapon: "polearm", vision: "pyro", nation: "liyue"});
        this.characters.set("jean", {weapon: "sword", vision: "anemo", nation: "mondstadt"});
        this.characters.set("kaedehara kazuha", {weapon: "sword", vision: "anemo", nation: "inazuma"});
        this.characters.set("kaeya", {weapon: "sword", vision: "cryo", nation: "mondstadt"});
        this.characters.set("kamisato ayaka", {weapon: "sword", vision: "cryo", nation: "inazuma"});
        this.characters.set("kamisato ayato", {weapon: "sword", vision: "hydro", nation: "inazuma"});
        this.characters.set("keqing", {weapon: "sword", vision: "electro", nation: "liyue"});
        this.characters.set("klee", {weapon: "catalyst", vision: "pyro", nation: "mondstadt"});
        this.characters.set("kujou sara", {weapon: "bow", vision: "electro", nation: "inazuma"});
        this.characters.set("lisa", {weapon: "catalyst", vision: "electro", nation: "mondstadt"});
        this.characters.set("mona", {weapon: "catalyst", vision: "hydro", nation: "mondstadt"});
        this.characters.set("ningguang", {weapon: "catalyst", vision: "geo", nation: "liyue"});
        this.characters.set("noelle", {weapon: "claymore", vision: "geo", nation: "mondstadt"});
        this.characters.set("qiqi", {weapon: "sword", vision: "cryo", nation: "liyue"});
        this.characters.set("raiden shogun", {weapon: "polearm", vision: "electro", nation: "inazuma"});
        this.characters.set("razor", {weapon: "claymore", vision: "electro", nation: "mondstadt"});
        this.characters.set("rosaria", {weapon: "polearm", vision: "cryo", nation: "mondstadt"});
        this.characters.set("sangonomiya kokomi", {weapon: "catalyst", vision: "hydro", nation: "inazuma"});
        this.characters.set("sayu", {weapon: "claymore", vision: "anemo", nation: "inazuma"});
        this.characters.set("shenhe", {weapon: "polearm", vision: "cryo", nation: "liyue"});
        this.characters.set("sucrose", {weapon: "catalyst", vision: "anemo", nation: "mondstadt"});
        this.characters.set("tartaglia", {weapon: "bow", vision: "hydro", nation: "liyue"});
        this.characters.set("thoma", {weapon: "polearm", vision: "pyro", nation: "inazuma"});
        this.characters.set("venti", {weapon: "bow", vision: "anemo", nation: "mondstadt"});
        this.characters.set("xiangling", {weapon: "polearm", vision: "pyro", nation: "liyue"});
        this.characters.set("xiao", {weapon: "polearm", vision: "anemo", nation: "liyue"});
        this.characters.set("xingqiu", {weapon: "sword", vision: "hydro", nation: "liyue"});
        this.characters.set("xinyan", {weapon: "claymore", vision: "pyro", nation: "liyue"});
        this.characters.set("yae miko", {weapon: "catalyst", vision: "electro", nation: "inazuma"});
        this.characters.set("yanfei", {weapon: "catalyst", vision: "pyro", nation: "liyue"});
        this.characters.set("yoimiya", {weapon: "bow", vision: "pyro", nation: "inazuma"});
        this.characters.set("yun jin", {weapon: "polearm", vision: "geo", nation: "liyue"});
        this.characters.set("zhongli", {weapon: "polearm", vision: "geo", nation: "liyue"});


        this.MAX_ATTEMPT = 5;
        this.play_again = true;
        this.playerText = "";
        this.guess = "";
        this.gpos = 42 + 32;
        this.guessed = false;
        this.wep = "";
        this.vis = "";
        this.nat = "";
        this.errorText = this.add.text(16, 16, 'Invalid Input', {fontSize: '32px', fill: '#000' });
        this.keys = Array.from(this.characters.keys());
        keyY = this.input.keyboard.addKeys(Phaser.Input.Keyboard.KeyCodes.Y);
        this.input.keyboard.on('keydown', (event) => {this.handleInput(event.key);});
        this.add.text(540, 10, "Genshin Wordle", { fontSize: '32px', fill: '#FFF' }).setOrigin(0.5,0);
        this.add.text(540, this.gpos - 32, "Guess the character: ", { fontSize: '32px', fill: '#FFF'}).setOrigin(0.5,0);
        this.playerTextDisplay = this.add.text(540, this.gpos, this.playerText, { fontSize: '32px', fill: '#FFF' }).setOrigin(0.5,0);
        this.ans = this.keys[Phaser.Math.Between(0, this.characters.size - 1)];
        this.attempt = this.MAX_ATTEMPT;
    }
    update() {
        if (this.play_again == true) {
            if (this.attempt >= 0) {
                console.log(this.guess);
                if (this.guessed) {
                    if (!this.characters.has(this.guess)) {
                        this.errorText = this.add.text(16, 16, 'Invalid Input', {fontSize: '32px', fill: '#FFF' });
                        this.guess = "";
                        this.playerTextDisplay.text ="";
                    } else {
                        if (!(this.guess == this.ans)) {
                            if (this.characters.get(this.guess).weapon == this.characters.get(this.ans).weapon) {
                                this.wep = "O";
                            } else {
                                this.wep = "X";
                            }
                            if (this.characters.get(this.guess).vision == this.characters.get(this.ans).vision) {
                                this.vis = "O";
                            } else {
                                this.vis = "X";
                            }
                            if (this.characters.get(this.guess).nation == this.characters.get(this.ans).nation) {
                                this.nat = "O";
                            } else {
                                this.nat = "X";
                            }
                            this.add.text(540, this.gpos, this.guess + ":\t" + this.wep + " weapon\t" + this.vis + " vision\t" + this.nat + " nation\t" + this.attempt + " guesses left", { fontSize: '32px', fill: '#FFF' }).setOrigin(0.5,0);
                        } else {
                            this.add.text(540, this.gpos, "correct :D", { fontSize: '32px', fill: '#FFF' }).setOrigin(0.5,0);
                            this.playerTextDisplay.setColor('#000');
                            this.playerTextDisplay.y = this.gpos + 64;
                            this.play_again = false;
                            this.add.text(540, this.gpos + 32, "play again? (y/n)", { fontSize: '32px', fill: '#FFF' }).setOrigin(0.5,0);
                        }
                        this.guess = "";
                        this.playerTextDisplay.y = this.gpos + 32;
                        this.attempt--;
                        this.gpos += 32;
                    }
                    this.guessed = false;
                }
            }
            if (this.attempt == -1) {
                this.add.text(540, this.gpos, "game over, answer was " + this.ans, { fontSize: '32px', fill: '#FFF' }).setOrigin(0.5,0);
                this.play_again = false;
                this.playerText = "";
                this.add.text(540, this.gpos + 32, "play again? (y/n)", { fontSize: '32px', fill: '#FFF' }).setOrigin(0.5,0);
                this.playerTextDisplay.setColor('#000');
                this.playerTextDisplay.y = this.gpos + 64;
            }
        }
    }
    handleInput(key) {
        this.errorText.setColor('#000');
        if (this.isLetter(key) || key == " ") {
            this.playerText = this.playerText + key;
        }
        if (key == "Backspace") {
            if (this.playerText.length > 0) {
                this.playerText=this.playerText.slice(0, this.playerText.length - 1);
            }
        }
        if (key == "Enter") {
            this.guessed = true;
            this.guess = this.playerText;
            this.playerText = "";
        }
        this.playerTextDisplay.text = this.playerText;
        if (this.play_again == false) {
            if (this.playerText == "y") {
                this.scene.restart();
            }
        }
    }

    // func found at https://www.codegrepper.com/code-examples/javascript/javascript+check+if+a-z+A-Z
    isLetter(str) {
        return str.length === 1 && str.match(/[a-z]/i);
    }
}