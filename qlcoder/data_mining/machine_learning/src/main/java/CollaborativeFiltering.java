import org.apache.mahout.cf.taste.common.TasteException;
import org.apache.mahout.cf.taste.impl.model.file.FileDataModel;
import org.apache.mahout.cf.taste.impl.recommender.svd.ExpectationMaximizationSVDFactorizer;
import org.apache.mahout.cf.taste.impl.recommender.svd.SVDRecommender;
import org.apache.mahout.cf.taste.model.DataModel;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

/**
 * Created by cheyulin on 10/19/16.
 */

public class CollaborativeFiltering {
    public static void main(String[] args) throws IOException, TasteException {

        File modelFile = new File("train.txt");

        DataModel model = new FileDataModel(modelFile);
        SVDRecommender svdrecommender = new SVDRecommender(model, new ExpectationMaximizationSVDFactorizer(model, 25, 100));
        BufferedReader bufferedReader = new BufferedReader(new FileReader("test.txt"));

        String line;
        while ((line = bufferedReader.readLine()) != null) {
            String item[] = line.split(",");
            try {
                System.out.print((int) Math.round(svdrecommender.estimatePreference(Long.parseLong(item[0]), Long.parseLong(item[1]))));
            }
            catch (Exception e){
                System.out.print(3);
            }
        }
    }


}
