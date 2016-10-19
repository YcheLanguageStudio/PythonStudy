import org.apache.mahout.cf.taste.common.TasteException;
import org.apache.mahout.cf.taste.impl.model.file.FileDataModel;
import org.apache.mahout.cf.taste.impl.neighborhood.NearestNUserNeighborhood;
import org.apache.mahout.cf.taste.impl.recommender.GenericUserBasedRecommender;
import org.apache.mahout.cf.taste.impl.recommender.svd.ExpectationMaximizationSVDFactorizer;
import org.apache.mahout.cf.taste.impl.recommender.svd.SVDRecommender;
import org.apache.mahout.cf.taste.impl.similarity.PearsonCorrelationSimilarity;
import org.apache.mahout.cf.taste.model.DataModel;
import org.apache.mahout.cf.taste.neighborhood.UserNeighborhood;
import org.apache.mahout.cf.taste.recommender.RecommendedItem;
import org.apache.mahout.cf.taste.recommender.Recommender;
import org.apache.mahout.cf.taste.similarity.UserSimilarity;

import java.io.File;
import java.io.IOException;
import java.util.List;

/**
 * Created by cheyulin on 10/19/16.
 */
public class CollaborativeFiltering {
    public static void main(String[] args) throws IOException, TasteException {

        File modelFile = new File("train.txt");

        DataModel model = new FileDataModel(modelFile);

        UserSimilarity similarity = new PearsonCorrelationSimilarity(model);

        UserNeighborhood neighborhood = new NearestNUserNeighborhood(4, similarity, model);

        Recommender recommender = new GenericUserBasedRecommender(model, neighborhood, similarity);


        SVDRecommender svdrecommender=new SVDRecommender(model,new ExpectationMaximizationSVDFactorizer(model,4,1000));

        //给用户436821推荐1个物品
        List<RecommendedItem> recommendations = recommender.recommend(436821, 1);

        for (RecommendedItem recommendation : recommendations) {
            System.out.println(recommendation);
        }
    }


}
