import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-lesson-page',
  templateUrl: './lesson-page.component.html',
  styleUrl: './lesson-page.component.css'
})
export class LessonPageComponent implements OnInit {
  words: { Word: string, Definition: string}[] = []

  ngOnInit(): void {
    this.words = [
      { Word: 'Chrissy', Definition: 'Christmas' },
      { Word: 'Daggy', Definition: 'Unfashionable' },
      { Word: 'Esky', Definition: 'Cooler or portable icebox' },
      { Word: 'G\'day', Definition: 'Hello' },
      { Word: 'Maccas', Definition: 'McDonald\'s' },
      { Word: 'No worries', Definition: 'No problem' },
      { Word: 'Ripper', Definition: 'Excellent' },
      { Word: 'Servo', Definition: 'Service station or gas station' },
      { Word: 'Thongs', Definition: 'Flip-flops' },
      { Word: 'Ute', Definition: 'Utility vehicle or pickup truck' },
      { Word: 'Yabby', Definition: 'Freshwater crayfish' },
      { Word: 'Breather', Definition: 'Short break' },
      { Word: 'Dunny', Definition: 'Toilet' },
      { Word: 'Footy', Definition: 'Football, usually Australian Rules Football' },
      { Word: 'Jumper', Definition: 'Sweater or jersey' },
      { Word: 'Mate', Definition: 'Friend' },
      { Word: 'Op shop', Definition: 'Opportunity shop or thrift store' },
      { Word: 'She\'ll be right', Definition: 'It will be okay' },
      { Word: 'Bogan', Definition: 'Unsophisticated person' },
      { Word: 'Coppers', Definition: 'Police officers' },
      { Word: 'Esky', Definition: 'Portable cooler' },
      { Word: 'Grog', Definition: 'Alcohol' },
      { Word: 'Joey', Definition: 'Baby kangaroo' },
      { Word: 'Mozzie', Definition: 'Mosquito' },
      { Word: 'Snags', Definition: 'Sausages' },
      { Word: 'Tinnie', Definition: 'Can of beer or small aluminum boat' },
      { Word: 'Chuck a sickie', Definition: 'Take a fake sick day' }
    ]
  }
}
