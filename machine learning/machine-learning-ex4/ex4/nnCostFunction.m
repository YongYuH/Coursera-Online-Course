function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

% Setup some useful variables
m = size(X, 1);
         
% You need to return the following variables correctly 
J = 0;
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));

% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m
%
% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a 
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the 
%               first time.
%
% Part 3: Implement regularization with the cost function and gradients.
%
%         Hint: You can implement this around the code for
%               backpropagation. That is, you can compute the gradients for
%               the regularization separately and then add them to Theta1_grad
%               and Theta2_grad from Part 2.
%

% Tips from forum :
% Let :
% m(5000) = the number of training examples
% n(401) = the number of training features, including the initial bias unit.
% h(25) = the number of units in the hidden layer - NOT including the bias unit
% r(10) = the number of output classifications

% Forwardpropagation
a1 = [ones(m, 1) X];

z2 = a1 * Theta1'; % (m x n)¡E(n x h) --> (m x h)
a2 = sigmoid(z2);

a2 = [ones(m, 1) a2];

z3 = a2 * Theta2'; % (m x [h+1])¡E([h+1] x r) --> (m x r)
a3 = sigmoid(z3); 

%[M,p] = max(a3, [], 2);
h = a3;
for k=1:num_labels
    for i=1:m
        if(y(i) == k)
            y2(i,k) = 1;
        end
    end        
end
j = -y2.*log(h)-(1-y2).*log(1-h);
J = 1/m *sum(sum(j));

Regularized_term_for_J = lambda/(2*m) * (sum(sum(Theta1(:,2:size(Theta1,2)).^2)) + sum(sum(Theta2(:,2:size(Theta2,2)).^2)));

J = J + Regularized_term_for_J;

% Backpropagation
% step 1 : Set the input layer's values (a(1)) to the t-th training example x(t).
x = a1;
% step 2 : error term of layer 3
delta_3 = (a3 - y2); % (m x r)
% step 3 : error term of layer 2
delta_2 = (delta_3 * Theta2(:,2:end)) .* sigmoidGradient(z2); % (m x r)¡E(r x h) --> (m x h)
% step 4 : accumulate the gradient
DELTA_1 = delta_2'*a1;    % (h x m)¡E(m x n) --> (h x n)
DELTA_2 = delta_3'*a2;    % (r x m)¡E(m x [h+1]) --> (r x [h+1])    

Theta1_grad = 1/m * DELTA_1;    % (h x n)
Theta2_grad = 1/m * DELTA_2;    % (r x [h+1]) 

Theta1(:,1) = 0;
Regularized_term_for_grad1 = lambda/m .*(Theta1);
Theta2(:,1) = 0;
Regularized_term_for_grad2 = lambda/m .*(Theta2);

Theta1_grad = Theta1_grad + Regularized_term_for_grad1;
Theta2_grad = Theta2_grad + Regularized_term_for_grad2; 

% -------------------------------------------------------------

% =========================================================================

% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];


end
