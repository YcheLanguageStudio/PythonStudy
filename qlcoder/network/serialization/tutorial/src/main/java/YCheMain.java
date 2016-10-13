import java.io.FileInputStream;
import java.io.IOException;


/**
 * Created by cheyulin on 10/13/16.
 */
public class YCheMain {
    public static void main(String[] args) throws IOException {
        TaskJava.Task task = TaskJava.Task.parseFrom(new FileInputStream("/path/to/pb.data"));
        long count = 0;
        for(TaskJava.Task.Answer answer : task.getAnswerList()) {
            count += answer.getData();
            System.out.println(answer.getData());
        }
        System.out.println(count);
    }
}
