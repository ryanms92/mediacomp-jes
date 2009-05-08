import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;

/**
 * The JES Config Class
 * Created for the Jython Environment for Students
 * The JESConfig Class reads the config file information for the JES
 * config file, located at JES_CONFIG_FILE_NAME
 */
public class JESConfig
{
	// Configuration Array Location Values
	public static final String JES_CONFIG_FILE_NAME = "JESConfig.txt";
	public static final int CONFIG_NAME = 0;
	public static final int CONFIG_GT = 1;
	public static final int CONFIG_MAIL = 2;
	public static final int CONFIG_MODE = 3;
	public static final int CONFIG_FONT = 4;
	public static final int CONFIG_EMAIL_ADDR = 5;
	public static final int CONFIG_GUTTER = 6;
	public static final int CONFIG_BLOCK = 7;
	public static final int CONFIG_WEB_TURNIN = 8;
	public static final int CONFIG_AUTOSAVEONRUN = 9;
	public static final int CONFIG_AUTOOPENDOC = 10;
	public static final int CONFIG_WRAPPIXELVALUES = 11;
	public static final int CONFIG_SKIN = 12;
	public static final int CONFIG_SHOWTURNIN = 13;
	public static final int CONFIG_BACKUPSAVE = 14;
	public static final int CONFIG_LOGBUFFER = 15;
	public static final int CONFIG_MEDIAPATH = 16;
	public static final int CONFIG_NLINES = 17;

	// Instance for the singleton pattern
	private static JESConfig theInstance = null;

	// Other instance variables
	private ArrayList<String> properties;
	private String[] defaults = {"","","","Normal","12","","1","0","","0","","1","","0","1","1",""};

	private JESConfig()
	{
		properties = readConfig();
		if ( properties == null )
		{
			properties = new ArrayList<String>( Arrays.asList( defaults ) );
		}

		if (getStringProperty( CONFIG_MEDIAPATH ) == "" )
			setStringProperty( CONFIG_MEDIAPATH, System.getProperty("user.home") );
	}

	public static JESConfig getInstance()
	{
		if (theInstance == null)
			theInstance = new JESConfig();
		
		return theInstance;	
	}

	public String getStringProperty( int property )
	{
		if ( ( property >= 0 ) && ( property < CONFIG_NLINES ) )
			return properties.get( property );
		else
			return "";
	}

	public boolean getBooleanProperty( int property )
	{
		String val = getStringProperty(property);
		return val.equals("1") ? true : false;
	}

	public int getIntegerProperty( int property )
	{
		
		String val = getStringProperty(property);
		if (!val.equals(""))
			return Integer.parseInt(val);
		else
			//TODO:  default value?  But this shouldn't happen says Buck
			return 0;
	}


	public void setStringProperty( int property, String value )
	{
		if ( ( property >= 0 ) && ( property < CONFIG_NLINES ) )
			properties.set( property, value );
	}

	public void setIntegerProperty( int property, int value )
	{
		setStringProperty(property, value + "");
	}

	public void setBooleanProperty( int property, boolean value )
	{
		setStringProperty(property, value ? "1" : "0");
	}

	private ArrayList<String> readConfig()
	{
		ArrayList<String> properties = null;
		try
		{
			String inputFileName =
			System.getProperty("user.home") +
			File.separatorChar + JES_CONFIG_FILE_NAME;
			File inputFile = new File(inputFileName);
			FileInputStream in = new
			FileInputStream(inputFile);

			byte bt[] = new
			byte[(int)inputFile.length()];
			in.read(bt);
			String s = new String(bt);
			in.close();
			properties = new ArrayList<String>(Arrays.asList(s.split("\r\n|\r|\n")));
			//you must be upgrading; adding blanks...
			while ( properties.size() < CONFIG_NLINES )
				properties.add("");
		}
		catch(java.io.IOException e)
		{
		        System.out.println( "Cannot access JESConfig file," + JES_CONFIG_FILE_NAME );
				  System.out.println(e);
		}
		return properties;
	}


	// Main for testing		
	public static void main( String[] args )
	{
		JESConfig jConfig = JESConfig.getInstance();
		for( int i = 0; i < CONFIG_NLINES; i++ )
		{
			System.out.println( jConfig.getStringProperty( i ) );
		}
	
	}


}
