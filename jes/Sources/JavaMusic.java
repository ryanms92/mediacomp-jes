import javax.sound.midi.*;
import java.io.*;

public class JavaMusic {
    
    private static Synthesizer synthr;
    private static MidiChannel channel;

    public static void open(){
	//Sequencer seqr = MidiSystem
	try{
	    synthr = MidiSystem.getSynthesizer();
	    synthr.open();
	    //Instrument[] instruments = sb.getInstruments();
	    //Instrument instr = instruments[0];
	    MidiChannel[] channels = synthr.getChannels();
	    channel = channels[0];
	    
	}catch(Exception e){

	}
    }

    public static void close(){
	synthr.close();
    }

    public static void cleanUp(){
	getChannel().allNotesOff();
    }
    
    public static MidiChannel getChannel(){
	if (channel == null){
	    open();
	}
	return channel;
    }

    public static void playNote(int note, int duration, int intensity){
	try{
	    getChannel().noteOn(note, intensity);
	    Thread.currentThread().sleep(duration);
	    getChannel().noteOff(note, intensity);
	}catch(InterruptedException e){}
    }

    public static void playNote(int note, int duration){
	playNote(note, duration, 64);
    }

    public static void main(String[] argv){
        playNote(66, 1000);
	playNote(68, 1000);
	playNote(70, 1000);
	playNote(71, 1000);
	playNote(73, 1000);
	playNote(75, 1000);
	playNote(77, 1000);
	playNote(78, 1000);
	close();
	System.exit(0);
    }
}
