/**
 * Created by cheyulin on 10/22/16.
 */

import org.apache.thrift.TException;
import org.apache.thrift.protocol.TBinaryProtocol;
import org.apache.thrift.protocol.TProtocol;
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TSocket;
import qlcoder.Auth;
import qlcoder.Task;
import qlcoder.Type;

public class ThirftStudy {
    public static void main(String[] args) {
        try {
            //Server Ip and port information
            TTransport transport = new TSocket("121.201.63.168", 9090, 30000);

            //Binary Protocol
            TProtocol protocol = new TBinaryProtocol(transport);

            //Rpc Interface
            Task.Client client = new Task.Client(protocol);

            //Open Socket
            transport.open();

            System.out.println(client.getTaskInfo(new Auth("cheyulin", Type.GET_ANSWER)));

            //Close Socket
            transport.close();
        } catch (TException x) {
            x.printStackTrace();
        }
    }
}
