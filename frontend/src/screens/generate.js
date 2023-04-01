import {MusicPlayer} from "../components/music_player";

export const GenerateMusic = () => {
    const playList = [
        {
            name: 'name',
            writer: 'writer',
            img: 'image.png',
            src: 'music.mp3',
            id: 1,
        },
    ]

    return <div>
        <MusicPlayer/>
    </div>
}