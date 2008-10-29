import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

class SplashWindow extends JWindow
{

    public static Frame splash(String filename) {
        Frame frame = new Frame();
        SplashWindow splash = new
            SplashWindow(filename, frame);

        return frame;
    }

    public SplashWindow(String filename, Frame f)
    {
        super(f);
        JLabel l = new JLabel(new ImageIcon(filename));
        getContentPane().add(l, BorderLayout.CENTER);
        pack();
        Dimension screenSize =
          Toolkit.getDefaultToolkit().getScreenSize();
        Dimension labelSize = l.getPreferredSize();
        setLocation(screenSize.width/2 - (labelSize.width/2),
                    screenSize.height/2 - (labelSize.height/2));
        addMouseListener(new MouseAdapter()
            {
                public void mousePressed(MouseEvent e)
                {
                    setVisible(false);
                    dispose();
                }
            });
        setVisible(true);
    }
}

