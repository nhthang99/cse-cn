import java.net.InetAddress;
import java.net.UnknownHostException;

/**
 * HostInfo
 */
public class HostInfo {

    public static void main(String[] args) {
        HostInfo host = new HostInfo();
        host.init();
    }
    public void init(){
        try {
            InetAddress myHost = InetAddress.getLocalHost();
            System.out.println(myHost.getHostAddress());
        } catch (UnknownHostException e) {
            System.out.println("Can not find localhost");
        }
    }
}